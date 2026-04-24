**English** · [한국어](./security-program-playbook.ko.md) · [Español](./security-program-playbook.es.md) · [日本語](./security-program-playbook.ja.md)

# Security program playbook for AI-accelerated offense

A consolidated rollout playbook distilled from the April 10, 2026 post [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) by Anthropic's Security Engineering and Research teams. The post's guidance maps directly onto existing SOC 2 and ISO 27001 controls. Nothing here is invented.

## Framing

AI is changing the speed at which vulnerabilities are found and exploited. Earlier in the same week, Anthropic announced Project Glasswing using Claude Mythos Preview for defensive cybersecurity. Within the next 24 months, vast numbers of bugs that sat unnoticed — possibly for years — will be found by AI models and chained into working exploits. Defenders who adopt AI tools can move faster too. Below are the seven "what to do now" areas with how-to guidance, followed by advice on report quality and small-team simplifications.

## 1. Close the patch gap

AI models are very effective at recognizing the signatures of known, already-patched vulnerabilities in unpatched systems. Reversing a patch into a working exploit is mechanical analysis these models excel at, so the window between a patch being published and an exploit becoming available is shrinking.

- Patch everything on the **CISA Known Exploited Vulnerabilities (KEV) catalog** immediately. Anything on this list which is reachable from a network should be treated as an emergency.
- Use **EPSS** (Exploit Prediction Scoring System) to prioritize the rest; it provides a daily-updated probability that a CVE will be exploited in the next 30 days.
- Reduce time-to-patch on internet-exposed systems: **within 24 hours** of an exploit becoming available; within days for other vulnerabilities.
- Automate patch deployment and reboots where an automated update causing an outage is an acceptable risk. Manual approval steps add delay, and **delay is now the primary risk**.

**Practical tip.** Most cloud and OS vendors already ship patch automation; enabling it is often a simple configuration change. For container images and dependency manifests, several open-source scanners run as a single CI step and annotate CVEs with KEV and EPSS data, so prioritization is built in.

→ See the reusable [closing-the-patch-gap skill](../skills/closing-the-patch-gap/SKILL.md).

## 2. Prepare to handle a much higher volume of vulnerability reports

Your Vulnerability Management process should plan for many more patches, from vendors and upstream.

- Plan for an **order-of-magnitude increase in finding volume.** If your security meetings are still built around a spreadsheet and a weekly meeting, it's unlikely you'll keep up.
- Check the security of your open-source dependencies. Use **OpenSSF Scorecard**; it runs in CI and flags unmaintained packages and missing signals (branch protection, fuzzing coverage, signed releases, maintainer activity).
- Apply the same expectations to your vendors via third-party risk management: ask how they are preparing for accelerated exploit timelines and whether they are scanning their own code.

**Practical tip.** Look into tools that evaluate reachability of vulnerable code. Build automated processes that continuously deliver new updates, with regression testing to gain confidence in fast deployment.

**AI leverage points in vulnerability management:**
- *Speeding up triage.* A frontier model can deduplicate findings, estimate exposure from asset knowledge, and draft remediation tickets with pre-identified affected code paths.
- *Dependency redundancy check.* Most large codebases accumulate multiple libraries doing the same job (several HTTP clients; several JSON parsers). Pointing an LLM at a lockfile and asking which dependencies overlap (and what consolidation would look like) is a one-hour exercise that often pays off.
- *Upgrade automation.* Frontier models can generate patches alongside vulnerability reports, test them, and accept upstream patches while validating tests pass.
- *AI vendoring.* For small dependencies that score poorly on OpenSSF Scorecard and are not actively maintained, consider having an LLM reimplement just the functionality you actually use.

## 3. Find bugs before you ship them

- Add **static analysis and AI-assisted code review** to CI; block merges on high-confidence findings. Address tooling (not the gate) if false positives make this impractical.
- **OWASP ASVS** defines what "passing" looks like at three levels of rigor.
- Add **automated penetration testing** to continuous delivery; run the same scanning against staging that attackers will run against production.
- **Secure the build pipeline.** The **SLSA** framework provides a graded path. OpenSSF publishes a reusable GitHub Actions workflow that produces SLSA Level 3 attestations, which is significantly less work than the SLSA spec suggests.
- Adopt **Secure by Design** practices (CISA's pledge: MFA by default; no default passwords; transparent vulnerability reporting) as a minimum bar.
- Prefer **memory-safe languages** (Rust, Go, managed runtimes) for new code. Existing C/C++ code does not need to be rewritten, but new C/C++ code should require a justification. AI-assisted rewrites are increasingly viable.

**Practical tip.** SAST tooling with OWASP Top 10 and language-specific rule sets is widely available, both open-source and built into code hosting platforms — CodeQL on GitHub is the most common starting point.

**AI leverage points at build-time:**
- *AI vulnerability scanning.* Scan your own code and systems with the same kind of model an attacker would use, before they do. Requires an isolated agent, a verification step to filter noise, and a path into the existing triage process. **If you implement one thing from this section, implement this.** → See the [vulnerability-scanning-agent](../agents/vulnerability-scanning-agent.md).
- *Patch generation.* A frontier model can usually propose a patch for a SAST or scanner finding. The developer's job shifts from "understand the bug and write a fix" to "verify a proposed fix is correct" — the latter is faster. Same approach applies to memory-safe migration: port a self-contained C module to Rust with tests, validate equivalence.

## 4. Find the vulnerabilities already in your code

Most long-running production code has been reviewed by humans many times but never examined by a frontier model. Proactively scanning identifies vulnerabilities within the reach of modern LLMs before attackers discover them.

- **Prioritize by exposure.** Start with code that parses untrusted input, enforces an auth decision, or is reachable from the internet.
- **Include legacy code.** Code predating current review practices often has the least recent scrutiny and the most to gain from a fresh pass.
- **Budget for remediation.** A model scan of older code typically produces fewer findings than a SAST rollout but a higher share of them are real. Plan engineering time.

**Practical tip.** Pick one internet-facing service with few current owners and scan its input handling and auth logic. Run the agent in isolation, add a verification step, and act on confirmed findings. One service done properly is a reasonable basis for estimating broader program cost.

## 5. Design for breach

Mitigations whose value comes from friction (making an attack tedious) are less effective against adversaries that can grind through the tedium. Favor controls that hold under unlimited attacker patience.

- **Adopt zero trust architecture.** Authenticate and authorize every request between services as if it came from the internet. Both **CISA's Zero Trust Maturity Model** and **NCSC's zero trust principles** offer staged adoption paths.
- **Tie access to verified hardware**, not credentials. Production systems and sensitive internal tools should only be reachable from managed employee devices with attested hardware identity, paired with **phishing-resistant 2FA (FIDO2 / passkeys)**. Stolen credentials alone should never be sufficient. Even service-to-service calls should root in hardware identity.
- **Isolate services by identity.**
- **Replace long-lived secrets with short-lived, narrowly-scoped tokens** issued by an identity provider. Static API keys and embedded credentials are among the first things an attacker with model-assisted code analysis will find.

**Practical tip.** Full zero-trust is a multi-year program, but an **identity-aware access proxy** puts device-verified, MFA-gated access in front of internal services without re-architecting them. Every major cloud provider offers a native option plus open-source / commercial alternatives. For secrets, move the single most widely-shared credential into a managed secrets store and rotate it — that's a useful forcing function for the rest.

## 6. Reduce and inventory what you expose

Two principles: you cannot defend what you don't know about, and smaller exposed surface means less to attack.

- Maintain a **current inventory** of every internet-facing host, service, and API endpoint. Include these in pentests and red-teaming.
- **Decommission unused systems.** Legacy services with no clear owner are typically also unpatched.
- **Minimize** what each service exposes. Default-deny network ingress; limit API surface to what is actually required.

**Practical tip.** Internet-wide scan indexes are publicly searchable — query one for your own IP ranges and domains to see what an attacker's reconnaissance sees. For cloud assets, native inventory tools (**AWS Config, Azure Resource Graph, GCP Asset Inventory**) already exist; the work is in querying them.

**AI leverage points for exposure:**
- *Pruning stale code and systems.* A model with read access to a codebase and traffic logs can list endpoints that have no callers and have not received traffic; from there, explain what removing each would affect.
- *Autonomous external red-teaming.* Point an AI offensive agent at your own perimeter from the outside, with no credentials and no source access. Catches what source scanning doesn't see: forgotten hosts, exposed management interfaces, default credentials, misconfigured storage. Run on the same cadence as inventory refresh. → See the [external-red-team-agent](../agents/external-red-team-agent.md).

## 7. Shorten your incident response time

Exploits can appear within hours of a patch. Response processes measured in days are too slow.

- **Put a model at the front of the alert queue.** Every inbound alert gets an automated first-pass investigation before a human sees it. A "triage agent" with read-only SIEM access directs attention to the alerts that need human judgement most. → See the [security-triage-agent](../agents/security-triage-agent.md).
- **Instrument dwell time and coverage first.** These are the two metrics AI automation can most move, and they matter most when exploit windows shorten.
- **Automate bookkeeping around incidents.** Models take notes, capture artifacts, pursue parallel investigation tracks, and draft the postmortem. **Humans** make containment, disclosure, and customer-comms calls. Human decision speed should never be rate-limited on evidence collection or write-ups.
- **Let models drive the detection flywheel** — ingesting threat intel, generating candidate detections, hunting, tuning what fires.
- **Run a tabletop for five simultaneous incidents.** The standard "one critical CVE on Monday" assumption may be unwise given AI capabilities. Stress-test with five incidents in the same week.
- **Map detection coverage against MITRE ATT&CK.** A standard vocabulary of attacker techniques. Knowing what you can and cannot detect is more useful than a generic "improve detection" goal. Prioritize coverage for lateral movement and credential access.
- **Establish emergency change procedures in advance.** A two-week change-approval cycle for production patches is itself a security risk. Same for containment actions (taking a service offline, rotating a credential, blocking a network path). Decide in advance who authorizes and how fast.

**Practical tip.** Pick one noisy rule with known-high false positive rate. Wire a frontier model into its alert stream with read-only access, have it produce a structured disposition for every firing, measure agreement against a human reviewer for two weeks. If agreement is tolerable, expand to the next rule. Do not try to automate the whole queue at once. Separately, **Atomic Red Team** is an open-source library of small, safe tests mapped to ATT&CK techniques; running a handful and checking which ones existing logging actually detected is a one-afternoon exercise that produces a concrete coverage map.

## Submitting vulnerability reports to others

If you are scanning code (your own dependencies, open-source projects, vendor products) and reporting upstream, report quality determines whether anyone acts on the finding. Open-source maintainers are already receiving large volumes of low-quality automated reports, and many ignore anything that looks AI-generated. **A report should be sent only when a human has verified it and is willing to put their name on it.**

See the reusable [writing-quality-vuln-reports skill](../skills/writing-quality-vuln-reports/SKILL.md) for the submission checklist and self-check.

## If you don't have a security team

Most advice above assumes a dedicated security function. Solo developers, open-source maintainers, and small organizations: the risks apply but actions are simpler.

- **Turn on automatic updates** for OS, browser, every application that offers it. Single most effective action available; no ongoing effort.
- **Prefer managed services over self-hosting.** Letting a provider with a security team run the database, auth, and email shifts the patching burden to them. Usually cheaper than one incident.
- **Use passkeys or hardware security keys** on every account that supports them. SMS codes can be intercepted; passwords get reused; a hardware key cannot be phished.
- **Enable free security tooling** on your code host. GitHub's Dependabot, secret scanning, and CodeQL are free for public repositories and catch a meaningful share of what enterprise tools catch. Enabling takes minutes.
- If you maintain an open-source project, **publish a SECURITY.md** stating who to contact and what to expect. AI-assisted scanning means more reports — clear intake helps tell signal from noise and signals to good-faith reporters that their effort will not be wasted.

## Reference table

| Topic | Reference |
|---|---|
| Patch prioritization | CISA KEV Catalog, FIRST EPSS, CISA BOD 22-01 |
| Baseline controls | ACSC Essential Eight, CISA CPGs, CIS Controls v8, NCSC 10 Steps |
| Secure development | NIST SSDF (SP 800-218), OWASP ASVS, OWASP SAMM, CISA Secure by Design |
| Memory safety | CISA/NSA Memory Safe Roadmaps |
| Supply chain & build integrity | SLSA, OpenSSF Scorecards, CISA SBOM resources, NIST SP 800-161 |
| Zero trust | CISA Zero Trust Maturity Model, NIST SP 800-207, NCSC Zero Trust Principles |
| Detection & response | MITRE ATT&CK, MITRE D3FEND |
| Program framework | NIST Cybersecurity Framework 2.0, NCSC Cyber Assessment Framework |

## Acknowledgements

The source post was written by members of Anthropic's Security Engineering and Research teams, including Donny Greenberg, Jason Clinton, Michael Moore, Abel Ribbink, and Jackie Bow, with contributions from Jannet Park, Gabby Curtis, and Stuart Ritchie.

## Source

[Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (published 2026-04-10).
