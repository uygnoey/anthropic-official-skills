[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Usar Subagentes en Claude Code

## ¿Qué es esta habilidad?
Un subagente es una **instancia separada de Claude con su propia ventana de contexto**. Esta habilidad recoge los patrones para delegar investigación, trabajo en paralelo o revisiones con ojos frescos a subagentes, de modo que tu sesión principal se mantenga enfocada.

## Cuándo usar (señales claras)
- Tareas con mucha exploración (10+ archivos)
- 3 o más subtareas independientes
- Necesidad de una perspectiva fresca
- Verificación antes de hacer commit
- Flujos de trabajo en pipeline (diseño → implementación → pruebas)

## Cuándo NO usar
- Trabajo secuencial o con dependencias
- Ediciones simultáneas al mismo archivo
- Tareas pequeñas donde el coste supera el beneficio
- Cuando los agentes deben coordinarse entre sí — los subagentes no pueden comunicarse; usa Agent Teams

## Cuatro formas de invocarlos

### A. Conversacional
```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

### B. Archivo de subagente personalizado (`.claude/agents/`)
```markdown
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities, injection risks, auth issues, and sensitive data exposure. Use proactively before commits touching auth, payments, or user data.
tools: Read, Grep, Glob
model: sonnet
---

You are a security-focused code reviewer. Analyze the provided changes for:
- SQL injection, XSS, and command injection risks
- Authentication and authorization gaps
- Sensitive data in logs, errors, or responses
- Insecure dependencies or configurations

Return a prioritized list of findings with file:line references and a recommended fix for each.
Be critical. If you find nothing, say so explicitly rather than inventing issues.
```
Invocación: `Have the security-reviewer look at the staged changes.`

### C. Política en CLAUDE.md
```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md
```

### D. Habilidad como comando slash
`.claude/skills/deep-review/SKILL.md` → ejecutar con `/deep-review`.

## Cuatro patrones prácticos
1. **Research-before-implement** — explora el área primero, luego codifica
2. **Parallel edits** — archivos independientes corregidos simultáneamente
3. **Fresh-eyes review** — tras la implementación, un subagente de solo lectura verifica
4. **Pipeline** — diseño / implementación / pruebas gestionados por distintos subagentes

## Consejos operativos
- `Ctrl+B` — envía un subagente al segundo plano.
- `/tasks` — inspecciona los subagentes en ejecución.
- No sobrecargues de especialistas; demasiados candidatos desestabilizan la delegación automática.
- Los subagentes no pueden comunicarse entre sí. Usa Agent Teams cuando sea necesario.

## Recursos incluidos
- Skills (2): `skills/using-subagents/SKILL.md`, `skills/deep-review/SKILL.md`
- Agent (1): `agents/security-reviewer.md`
- Hook (1): `hooks/check-tests.json` / `hooks/check-tests.md`

## Fuente
Basado en [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) (publicado el 2026-04-07). Consulta el original para una orientación autorizada.
