[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post anuncia la disponibilidad en beta pública de memoria integrada basada en sistema de archivos para Claude Managed Agents.

## ¿Cuándo es útil?
Es útil cuando quieres agentes en producción que mejoren entre sesiones sin tener que construir y operar tu propia infraestructura de memoria.

## Puntos clave
- La memoria está pensada para agentes de larga duración que aprenden entre sesiones y pueden compartir aprendizajes entre agentes.
- La memoria se monta directamente en un sistema de archivos, para que los agentes la gestionen con herramientas conocidas (bash y ejecución de código).
- Los recuerdos son archivos portables con controles de nivel empresarial (permisos por ámbito, registros de auditoría, exportación/rollback/redacción y gestión programática vía API).
- Las actualizaciones aparecen como eventos de sesión en la Claude Console para facilitar la trazabilidad.

## Recursos incluidos
- Skill: managed-agents-memory-overview (resumen conceptual y consideraciones de implementación)
- Guide: managed-agents-memory (lista de verificación de despliegue/operaciones)

## Fuente
https://claude.com/blog/claude-managed-agents-memory
