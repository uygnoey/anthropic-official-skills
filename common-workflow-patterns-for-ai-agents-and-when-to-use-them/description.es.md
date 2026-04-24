[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post explica tres patrones de flujo de trabajo probados en producción para agentes de IA—secuencial, paralelo y evaluador–optimizador—y cómo elegir entre ellos.

## ¿Cuándo es útil?
Es útil cuando diseñas sistemas de agentes en varios pasos y necesitas equilibrar latencia, costo y fiabilidad eligiendo un patrón de ejecución adecuado.

## Puntos clave
- Empieza simple: prueba primero con un solo agente y adopta flujos de trabajo solo si hace falta.
- El flujo secuencial encaja con dependencias, pero añade latencia.
- El flujo paralelo reduce el tiempo total para subtareas independientes, pero requiere una estrategia de agregación y puede aumentar el costo.
- El patrón evaluador–optimizador mejora la calidad con iteración, pero consume más tokens y necesita criterios claros de parada.

## Recursos incluidos
- Una "lista de decisión" y descripciones de patrones convertidas en un Agent Skill.

## Fuente
- https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
