[English](./claude-code-plugins-overview.en.md) · [한국어](./claude-code-plugins-overview.ko.md) · **Español** · [日本語](./claude-code-plugins-overview.ja.md)

## ¿Qué es un plugin de Claude Code?
Un plugin es un bundle ligero para empaquetar y compartir personalizaciones de Claude Code.

## ¿Qué puede incluir un plugin?
Un plugin puede agrupar cualquier combinación de:
- comandos con barra
- subagentes
- servidores MCP
- hooks

## ¿Por qué usar plugins?
- Estandarizar entornos (mejores prácticas del equipo).
- Compartir flujos de trabajo (debug, despliegues, arnés de pruebas).
- Conectar herramientas (vía servidores MCP).
- Activar/desactivar capacidades según necesidad para reducir el contexto del prompt del sistema.

## Primeros pasos
Desde Claude Code (beta pública):
1. Añadir un marketplace: `/plugin marketplace add <user-or-org>/<repo-name>`
2. Instalar un plugin: `/plugin install <plugin-name>`

## Fuente
- https://claude.com/blog/claude-code-plugins
