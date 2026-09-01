---
name: school-district-rollout
description: Move a K-12 school or district from individually verified teacher accounts to a centrally managed Claude for Teachers account — verifying the district, accepting the K-12 terms, connecting the email domain and single sign-on, and understanding what changes for teachers already using it. Use when planning a district-wide rollout, when checking eligibility and the free-access window, when confirming FERPA posture and student data handling before approving a deployment, or when deciding which teaching capabilities to introduce first.
---

# School district rollout

Claude for Teachers is available to schools and districts as a free Enterprise offering.
Organizations that qualify and register by **June 30, 2027** receive one year of complimentary
access.

The shift this enables is administrative, not instructional: teachers who verified individually keep
working, but the district gains centrally managed accounts with enterprise controls and
district-level terms covering student data.

## Instructions

### 1. Confirm the district qualifies and note the window

The offering is for K-12 schools and districts. Registration must happen by June 30, 2027 to receive
the year of complimentary access. Treat that date as the planning constraint — it bounds when the
verification and SSO work has to be finished, not when teachers must start using it.

### 2. Work through the four setup steps in order

The rollout is a short sequence and each step depends on the one before it:

1. **Verify the district.** Establish that the organization is a qualifying K-12 school or district.
2. **Accept the K-12 terms.** These are the district-level terms, including the data processing
   agreement that covers student information.
3. **Connect the email domain.** This is what associates existing teacher accounts with the
   district.
4. **Connect single sign-on.** Enterprise access lands here, alongside role-based access controls.

### 3. Plan for teachers who are already verified

Teachers already verified on the district's domain **transfer automatically** to the centralized
account once the domain is connected. Nobody re-registers.

Say this explicitly in the rollout communication. The most common confusion in a domain-based
migration is teachers assuming they need to do something; here they do not.

### 4. Settle the data questions before, not after

Student data is not used for model training, and student information is protected by the K-12 Data
Processing Agreement. FERPA compliance is maintained through the district-level terms and the DPA.

Bring these to whoever owns privacy review in the district early — they are the questions that
otherwise stall an approved rollout at the last step. See
[references/compliance-and-eligibility.md](references/compliance-and-eligibility.md) for the details
to hand over.

### 5. Introduce capabilities deliberately

Do not open with "here is Claude." Open with the two teaching skills, because they map to work
teachers already do:

- **Lesson Preparation** — helps educators plan key instructional moments.
- **Check for Understanding** — creates standards-aligned assessments, available for mathematics
  first.

Teaching skills are aligned with state academic standards across all 50 states, so a district can
frame adoption in terms of its own standards rather than in terms of a tool.

[references/teaching-capabilities.md](references/teaching-capabilities.md) lists what shipped in the
back-to-school update, including the accessibility and lesson planning improvements.

### 6. Choose the pilot by standards coverage

Where the standards alignment is strongest, the first cohort has the least friction. Check for
Understanding starts with mathematics — a math department is therefore a lower-risk first cohort
than one whose subject is not yet covered by the assessment skill.

## Examples

**A district with scattered individual accounts.** Teachers across several schools verified
individually over the past year. The district verifies, accepts the K-12 terms, connects its email
domain, and connects SSO. Every teacher on the domain moves to the centrally managed account without
re-registering; the district now has role-based access controls and district-level terms it did not
have before.

**A privacy review that would otherwise block approval.** The district's privacy officer asks how
student data is handled. The answer is on the record before the rollout starts: student data is not
used for model training, student information is covered by the K-12 Data Processing Agreement, and
FERPA compliance runs through district-level terms and the DPA.

**A first-cohort choice.** An instructional lead wants one department to start. Check for
Understanding is available for mathematics first, so the math team can use both teaching skills —
Lesson Preparation for planning and Check for Understanding for standards-aligned assessments —
while other departments start with lesson preparation alone.

## Source

<https://claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts> (2026-08-28)
