[English](./README.md) · [한국어](./README.ko.md) · **Español** · [日本語](./README.ja.md)

# skills-from-claude-blog

> Artefactos destilados de las publicaciones de [claude.com/blog](https://www.claude.com/blog),
> organizados según las especificaciones oficiales de extensión de Claude Code.
> Sin afiliación con Anthropic — proyecto de resumen de terceros.

Repositorio que convierte los posts oficiales del blog de Claude en **especificaciones oficiales de Claude Code según el carácter de cada post**. Un proceso por lotes se ejecuta cada 4 horas para incorporar los posts nuevos y los pendientes.

## Estructura (por post)

Un post = una carpeta `<YYYY.MM.DD>_<blog-slug>/` en la raíz del repositorio. El prefijo de fecha es el `published_date` del post convertido a `YYYY.MM.DD`, y `<blog-slug>` es el último segmento de la URL. Las carpetas se ordenan de forma natural de más reciente a más antigua en GitHub. Las subcarpetas aparecen de forma condicional según el carácter del post.

```
<YYYY.MM.DD>_<blog-slug>/
├── description.en.md               # Resumen en inglés (siempre)
├── description.ko.md               # Resumen en coreano (siempre)
├── description.es.md               # Resumen en español (siempre)
├── description.ja.md               # Resumen en japonés (siempre)
├── source.json                     # Metadatos de la fuente (siempre)
│
├── skills/<name>/SKILL.md          # A. Spec de Agent Skills
├── agents/<name>.md                # B. Spec de Claude Code Subagents
├── guides/<name>.{en,ko,es,ja}.md  # C. Guías libres multilingües
├── hooks/<name>.json +.md          # D. Hooks JSON + notas
├── output-styles/<name>.md         # E. Output Style
└── plugin/                         # G. Paquete de plugin (raro)
    ├── .claude-plugin/plugin.json
    └── skills|agents|hooks|output-styles/...
```

### Referencias oficiales
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — `SKILL.md`
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — `agents/<name>.md`
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks) — `hooks/<name>.json`
- [Output Styles](https://code.claude.com/docs/en/output-styles) — `output-styles/<name>.md`
- [Plugins](https://code.claude.com/docs/en/plugins) — paquete `plugin/`

### Matriz de selección de spec

| Veredicto | Pregunta disparadora | Artefacto |
|---|---|---|
| **A. Skill** | ¿El post describe un **patrón / principio / framework / how-to** reutilizable? | `skills/<name>/SKILL.md` |
| **B. Subagent** | ¿El post define explícitamente **2 o más roles de agente con nombre**? | cada `agents/<name>.md` |
| **C. Guide** | ¿Es un post de **despliegue / arquitectura / metodología / encuesta**? | `guides/<name>.{en,ko,es,ja}.md` |
| **D. Hook** | ¿El post automatiza un **evento del ciclo de vida** (PreToolUse, PostToolUse, Stop, SessionStart…)? | `hooks/<name>.json` + notas `.md` |
| **E. Output Style** | ¿Define un **cambio completo de tono/rol/formato del system prompt** (no un simple tip)? | `output-styles/<name>.md` |
| **G. Plugin** | ¿Se centra en **empaquetar varios artefactos para su distribución**? | paquete `plugin/` completo |

- **F. Slash Commands no se generan.** La documentación oficial marca `.claude/commands/` como legacy y recomienda `.claude/skills/`; los posts sobre slash commands se **convierten en Skills**.
- Es normal que varios veredictos apliquen a la vez. Genera todos.
- Ante la duda, **por defecto incluye A**. Los Skills son lo más reutilizable para el lector.
- **Nunca inventes roles, patrones o scripts que no estén en la fuente.** En caso de duda, cita la fuente.

## Uso directo

Cada artefacto puede copiarse tal cual a tu proyecto.

| Artefacto | Destino |
|---|---|
| `skills/<name>/` | `.claude/skills/<name>/` o `~/.claude/skills/<name>/` |
| `agents/<name>.md` | `.claude/agents/<name>.md` o `~/.claude/agents/<name>.md` |
| Contenido de `hooks/<name>.json` | Fusionar en el campo `hooks` de `.claude/settings.json` |
| `output-styles/<name>.md` | `.claude/output-styles/<name>.md` |
| `plugin/` | Cargar con `--plugin-dir ./plugin` |

## Índice

| Post | Publicado | Artefactos |
|---|---|---|
| [New connectors in Claude for everyday life](https://claude.com/blog/connectors-for-everyday-life) | 2026-04-23 | 1 skill |
| [Built-in memory for Claude Managed Agents](https://claude.com/blog/claude-managed-agents-memory) | 2026-04-23 | 1 skill + 1 guide |
| [Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) | 2026-04-22 | 1 skill |
| [Meet the winners of our Built with Opus 4.6 Claude Code hackathon](https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) | 2026-04-20 | 1 skill |
| [Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) | 2026-04-16 | 1 skill + 1 guide |
| [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) | 2026-04-15 | 1 skill + 1 guide |
| [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) | 2026-04-14 | 1 skill + 1 guide |
| [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign) | 2026-04-14 | 1 skill |
| [Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent) | 2026-04-10 | 1 skill |
| [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) | 2026-04-10 | 2 skill + 3 agent + 1 guide |
| [Multi-agent coordination patterns: Five approaches and when to use them](https://claude.com/blog/multi-agent-coordination-patterns) | 2026-04-10 | 1 skill + 1 guide |
| [The advisor strategy: Give agents an intelligence boost](https://claude.com/blog/the-advisor-strategy) | 2026-04-09 | 1 skill |
| [Making Claude Cowork ready for enterprise](https://claude.com/blog/cowork-for-enterprise) | 2026-04-09 | 1 skill |
| [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) | 2026-04-08 | 1 guide |
| [How Carta Healthcare gets AI to reason like a clinical abstractor](https://claude.com/blog/carta-healthcare-clinical-abstractor) | 2026-04-08 | 1 skill |
| [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) | 2026-04-07 | 2 skill + 1 agent + 1 hook |
| [Harnessing Claude's Intelligence: 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) | 2026-04-02 | 1 skill + 1 guide |
| [Audit Claude Platform activity with the Compliance API](https://claude.com/blog/claude-platform-compliance-api) | 2026-03-30 | 1 skill |
| [Auto mode for Claude Code](https://claude.com/blog/auto-mode) | 2026-03-24 | 1 skill |
| [Put Claude to work on your computer](https://claude.com/blog/dispatch-and-computer-use) | 2026-03-23 | 1 skill |
| [Code with Claude comes to San Francisco, London, and Tokyo](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo) | 2026-03-18 | 1 skill + 1 guide |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [Advancing Claude for Excel and PowerPoint](https://claude.com/blog/claude-excel-powerpoint-updates) | 2026-03-11 | 1 skill + 1 guide |
| [Common workflow patterns for AI agents](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them) | 2026-03-05 | 1 skill + 1 guide |
| [Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance) | 2026-02-24 | 1 guide |
| [Cowork and plugins for teams across the enterprise](https://claude.com/blog/cowork-plugins-across-enterprise) | 2026-02-24 | 1 guide |
| [How AI helps break the cost barrier to COBOL modernization](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization) | 2026-02-23 | 1 skill |
| [Behind the model launch: What customers discovered testing Claude Opus 4.6 early](https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early) | 2026-02-09 | 1 skill |
| [Customize Cowork with plugins - Claude.ai](https://claude.com/blog/cowork-plugins) | 2026-01-30 | 1 guide |
| [Measure Claude Code's impact with contribution metrics](https://claude.com/blog/contribution-metrics) | 2026-01-29 | 1 skill |
| [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) | 2026-01-29 | 1 skill + 1 guide |
| [Updates to Claude Team](https://claude.com/blog/claude-team-updates) | 2026-01-28 | 1 skill |
| [How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-marketing) | 2026-01-26 | 1 skill |
| [Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) | 2026-01-23 | 1 skill |
| [Building agents with Skills: Equipping agents for specialized work](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work) | 2026-01-22 | 1 skill + 1 guide |
| [Eight trends defining how software gets built in 2026](https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026) | 2026-01-21 | 1 skill |
| [Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) | 2025-12-19 | 1 skill |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [How Anthropic's legal team cut review times from days to hours with Claude](https://claude.com/blog/how-anthropic-uses-claude-legal) | 2025-12-08 | 1 skill |
| [Claude Code and Slack](https://claude.com/blog/claude-code-and-slack) | 2025-12-08 | 1 skill |
| [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [How three YC startups built their companies with Claude Code](https://claude.com/blog/building-companies-with-claude-code) | 2025-11-17 | 1 skill + 1 guide |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for startups](https://claude.com/blog/building-ai-agents-for-startups) | 2025-11-03 | 1 skill |
| [Building AI agents in healthcare and life sciences](https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences) | 2025-10-30 | 1 skill + 1 guide |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agent + 1 guide |
| [Fix software bugs faster with Claude](https://claude.com/blog/fix-software-bugs-faster-with-claude) | 2025-10-28 | 1 skill |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Build responsive web layouts](https://claude.com/blog/build-responsive-web-layouts) | 2025-10-10 | 1 skill |
| [Customize Claude Code with plugins](https://claude.com/blog/claude-code-plugins) | 2025-10-09 | 1 skill + 1 guide + 1 plugin |
| [Beyond permission prompts: making Claude Code more secure and autonomous](https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous) | 2025-10-08 | 1 skill |
| [How enterprises are driving AI transformation with Claude](https://claude.com/blog/driving-ai-transformation-with-claude) | 2025-10-01 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |
| [Managing context on the Claude Developer Platform](https://claude.com/blog/context-management) | 2025-09-29 | 1 skill |
| [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | 2025-09-29 | 1 skill |
| [Claude is now available in Microsoft 365 Copilot](https://claude.com/blog/claude-now-available-in-microsoft-365-copilot) | 2025-09-24 | 1 skill + 1 guide |
| [Claude can now create and edit files](https://claude.com/blog/create-files) | 2025-09-09 | 1 skill |
| [Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) | 2025-08-25 | 1 skill + 1 guide |
| [Claude Code and new admin controls for business plans](https://claude.com/blog/claude-code-and-new-admin-controls-for-business-plans) | 2025-08-20 | 1 skill |
| [Claude Sonnet 4 now supports 1M tokens of context](https://claude.com/blog/1m-context) | 2025-08-12 | 1 skill |
| [Automate security reviews with Claude Code](https://claude.com/blog/automate-security-reviews-with-claude-code) | 2025-08-06 | 1 skill |
| [Build and share AI-powered apps with Claude](https://claude.com/blog/claude-powered-artifacts) | 2025-07-25 | 1 skill |
| [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code) | 2025-07-24 | 1 skill |
| [Discover tools that work with Claude](https://claude.com/blog/connectors-directory) | 2025-07-14 | 1 skill |
| [Turn ideas into interactive AI-powered apps](https://claude.com/blog/build-artifacts) | 2025-06-25 | 1 skill |
| [Remote MCP support in Claude Code](https://claude.com/blog/claude-code-remote-mcp) | 2025-06-18 | 1 skill + 1 guide |
| [Mcp Connector](https://claude.com/blog/agent-capabilities-api) | 2025-05-22 | 1 skill |
| [Claude on Google Cloud’s Vertex AI: FedRAMP High and IL2 Authorized](https://claude.com/blog/claude-on-google-cloud-fedramp-high) | 2025-04-02 | 1 skill |
| [Introducing the analysis tool in Claude.ai](https://claude.com/blog/analysis-tool) | 2024-10-24 | 1 skill |
| [Claude for Enterprise](https://claude.com/blog/claude-for-enterprise) | 2024-09-10 | 1 skill + 1 guide |
| [Claude Android app](https://claude.com/blog/android-app) | 2024-07-16 | 1 skill |
| [Fine-tune Claude 3 Haiku in Amazon Bedrock](https://claude.com/blog/fine-tune-claude-3-haiku) | 2024-07-10 | 1 skill |
| [Evaluate prompts in the developer console](https://claude.com/blog/evaluate-prompts) | 2024-07-09 | 1 skill |
| [Long context prompting for Claude 2.1](https://claude.com/blog/claude-2-1-prompting) | 2023-12-06 | 1 skill |
| [Claude on Amazon Bedrock now available to every AWS customer](https://claude.com/blog/amazon-bedrock-general-availability) | 2023-09-28 | 1 skill |
| [Claude 2 on Amazon Bedrock](https://claude.com/blog/claude-2-amazon-bedrock) | 2023-08-23 | 1 skill |


Todas las guías y resúmenes están disponibles en inglés, coreano, español y japonés. Cambia de idioma con el selector en la parte superior de cada archivo.

## Operación por lotes

- Un cron de Perplexity Computer corre cada 4 horas.
- La lista de posts se obtiene de `https://www.claude.com/sitemap.xml` y el índice `/blog`.
- Prioridad: posts nuevos desde la última ejecución (más nuevo → más antiguo) → posts antiguos sin procesar (más antiguo → más nuevo) → fecha desconocida.
- Máximo 2 posts por ejecución.

## Guías de autoría

1. `SKILL.md` y `agents/*.md` siguen la spec oficial (en inglés).
2. Hook JSON refleja el comportamiento del post al pie de la letra; los comandos shell citan la fuente en comentarios.
3. Output Styles copian el tono/rol/formato indicado; si hay dudas, degradar a guide.
4. Campo `name` (Skill, Subagent, Output Style, Plugin): `^[a-z0-9-]+$`, ≤64 caracteres, palabras reservadas prohibidas: `claude`, `anthropic`.
5. `description` en tercera persona y ≤1024 caracteres (Skill / Subagent).
6. Las `guides/` se escriben en los cuatro idiomas (`.en.md`, `.ko.md`, `.es.md`, `.ja.md`) con selector de idioma arriba.
7. Los resúmenes humanos (`description.*.md`) cubren los mismos cuatro idiomas con selector de idioma.
8. **Nunca inventes contenido que no esté en la fuente.** Si no estás seguro, escribe "ver fuente".
9. **Los artifacts son autocontenidos.** `SKILL.md`, `agents/*.md`, `hooks/*.md` y `output-styles/*.md` no deben referenciar nada fuera de su propia carpeta — sin rutas `../`, sin enlaces entre artifacts, sin enlaces de vuelta a `description.*.md` o `guides/`. Si necesitas material externo, cópialo a un archivo companion local (`references/`, `examples/`, `templates/`, `scripts/`, `prompts/`, `assets/` o un `.md` hermano).

## Archivos

```
.
├── <YYYY.MM.DD>_<blog-slug>/           # Una carpeta por post, con prefijo de fecha
├── scripts/
│   ├── list_pending.py          # Lista de URLs pendientes
│   ├── mark_processed.py        # Marca una URL como procesada
│   ├── update_last_run.py       # Sella el timestamp del lote
│   └── validate.py              # Validador pre-commit para todas las specs
└── state/
    └── processed.json           # URLs procesadas + last_run_at
```

## Licencia

- Los posts originales (blog de Claude) son © Anthropic. Este repositorio contiene resúmenes y citas con fines de estudio y referencia.
- Código del repositorio: MIT License.
