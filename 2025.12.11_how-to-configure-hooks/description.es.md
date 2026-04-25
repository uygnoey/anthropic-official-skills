[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?

Este post explica cómo configurar hooks de Claude Code para automatizar pasos repetitivos, hacer cumplir reglas del proyecto e inyectar contexto en tus sesiones de programación.

## ¿Cuándo es útil?

Es útil cuando quieres que Claude Code ejecute comandos o inserte comprobaciones mediante prompts automáticamente en eventos clave del ciclo de vida (antes/después de usar herramientas, inicio/fin de sesión, compactación, eventos de parada, etc.).

## Puntos clave

- Los hooks se configuran con JSON que asigna eventos del ciclo de vida (por ejemplo: PreToolUse, PostToolUse, SessionStart, Stop) a una o más acciones.
- Las acciones pueden ejecutar comandos o comprobaciones basadas en prompts.
- Los matchers distinguen mayúsculas/minúsculas y varios hooks coincidentes pueden ejecutarse en paralelo.
- Los hooks se ejecutan con los permisos de tu usuario; valida/sanitiza stdin y ten cuidado con archivos sensibles.
- Hay un tiempo de espera predeterminado (60 segundos) configurable.

## Recursos incluidos

- Un script envoltorio reutilizable para registrar la entrada/salida del hook: `hooks/log-wrapper.sh`
- Configuraciones de ejemplo para patrones comunes:
  - Validar rutas antes de Write (`hooks/pretooluse-validate-write-path.json`)
  - Restringir comandos de tests vía PermissionRequest (`hooks/permissionrequest-validate-tests.json`)
  - Dar formato automáticamente tras Write/Edit (`hooks/posttooluse-format-written-files.json`)
  - Respaldar transcripciones antes de compactar (`hooks/precompact-backup-transcript.json`)
  - Mostrar contexto del proyecto en SessionStart (`hooks/sessionstart-show-context.json`)
  - Registrar sesiones en SessionStart (`hooks/sessionstart-log-session.json`)
  - Exigir una verificación de completitud en Stop (`hooks/stop-completion-check.json`)
  - Revisar salidas de subagentes en SubagentStop (`hooks/subagentstop-review.json`)
  - Inyectar contexto del sprint en UserPromptSubmit (`hooks/userpromptsubmit-inject-context.json`)

## Fuente

- https://claude.com/blog/how-to-configure-hooks
