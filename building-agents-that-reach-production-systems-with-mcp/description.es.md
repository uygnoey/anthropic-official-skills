[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Building agents that reach production systems with MCP

## ¿De qué trata este post?
Este post explica cómo los agentes basados en Claude pueden conectarse a sistemas y flujos de trabajo de producción, y cómo elegir el enfoque de integración adecuado según tus restricciones.

## ¿Cuándo es útil?
Es útil cuando necesitas que un agente acceda de forma segura y confiable a sistemas internos o de terceros (por ejemplo, trackers de incidencias, almacenes de datos o infraestructura), especialmente en entornos cloud/producción.

## Puntos clave
- Compara tres enfoques de integración: llamadas directas a APIs, automatización vía CLI y servidores de herramientas basados en MCP.
- En producción, los servidores MCP remotos pueden hacer que una integración sea reutilizable para muchos clientes y entornos.
- Diseña herramientas alrededor de la intención del usuario (no como espejos 1:1 de endpoints) y mantén una superficie compacta.
- Mejora la eficiencia de contexto cargando definiciones bajo demanda y procesando resultados grandes en código.
- Usa autenticación estandarizada (por ejemplo, OAuth) y patrones de almacenamiento de tokens para operar en producción.

## Recursos incluidos
- Agent Skill: `skills/mcp-production-integration-patterns/SKILL.md`

## Fuente
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
