[English](./README.md) · [한국어](./README.ko.md) · **Español** · [日本語](./README.ja.md)

# skills-from-claude-blog

> Artefactos destilados de las publicaciones de [claude.com/blog](https://www.claude.com/blog),
> organizados según las especificaciones oficiales de extensión de Claude Code.
> Sin afiliación con Anthropic — proyecto de resumen de terceros.

Repositorio que convierte los posts oficiales del blog de Claude en **especificaciones oficiales de Claude Code según el carácter de cada post**. Un proceso por lotes se ejecuta cada 4 horas para incorporar los posts nuevos y los pendientes.

## Estructura (por post)

Un post = una carpeta `<blog-slug>/`. Las subcarpetas aparecen de forma condicional según el carácter del post.

```
<blog-slug>/
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
| [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) | 2026-04-15 | 1 skill + 1 guide |
| [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) | 2026-04-14 | 1 skill + 1 guide |
| [Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) | 2026-04-16 | 1 skill + 1 guide |
| [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign) | 2026-04-14 | 1 skill |
| [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) | 2026-04-10 | 2 skills + 3 agents + 1 guide |
| [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) | 2026-04-08 | 1 guide |
| [Subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) | 2026-04-07 | 2 skills + 1 agent + 1 hook |
| [Harnessing Claude's Intelligence \| 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) | 2026-04-02 | 1 skill + 1 guide |
| [Auto mode for Claude Code](https://claude.com/blog/auto-mode) | 2026-03-24 | 1 skill |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [Using CLAUDE.md files](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agents + 1 guide |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |


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
├── <blog-slug>/                       # Una carpeta por post
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
