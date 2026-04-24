[English](./remote-mcp-overview.en.md) · [한국어](./remote-mcp-overview.ko.md) · **Español** · [日本語](./remote-mcp-overview.ja.md)

## ¿Qué es MCP remoto en Claude Code?
El soporte de MCP remoto permite que Claude Code se conecte a servidores MCP alojados por proveedores para usar herramientas y recursos de terceros directamente en tu flujo de trabajo.

## Por qué importa
- Menos mantenimiento que servidores locales (los proveedores gestionan actualizaciones, escalado y disponibilidad).
- Conexiones seguras mediante OAuth nativo.
- Permite a Claude Code incorporar contexto estructurado de sistemas externos (p. ej., trackers de issues o monitorización de errores).

## Flujo típico
1. Elegir un servidor MCP del proveedor.
2. Añadir la URL del proveedor en Claude Code.
3. Autenticar una vez (OAuth).
4. Usar las herramientas/recursos expuestos en el flujo de trabajo.

## Fuente
- https://claude.com/blog/claude-code-remote-mcp
