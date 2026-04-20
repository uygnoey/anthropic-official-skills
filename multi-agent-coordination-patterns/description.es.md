[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post recorre cinco patrones comunes de coordinación multiagente (generator-verifier, orchestrator-subagent, agent teams, message bus y shared state) y explica su mecánica, sus trade-offs y cómo elegir entre ellos.

## ¿Cuándo es útil?
Es útil cuando ya decidiste que un sistema multiagente tiene sentido y necesitas elegir (o evolucionar) una arquitectura de coordinación según la descomposición de tareas, los límites de contexto, el flujo de información y restricciones operativas.

## Puntos clave
- Empieza con el patrón más simple que pueda funcionar, observa dónde falla y evoluciona desde allí.
- Generator-verifier encaja con salidas críticas de calidad con criterios de evaluación explícitos y un límite de iteraciones.
- Orchestrator-subagent encaja con subtareas claras y acotadas, pero el orquestador puede convertirse en cuello de botella de información.
- Agent teams encaja con subtareas independientes y de larga duración con trabajadores persistentes, pero requiere una buena partición.
- Message bus encaja con pipelines basados en eventos y ecosistemas crecientes, pero complica el enrutamiento y la depuración.
- Shared state encaja con trabajo colaborativo donde los agentes comparten hallazgos directamente, pero necesita condiciones de terminación fuertes para evitar bucles reactivos.

## Recursos incluidos
- Skill: guía para elegir y aplicar patrones de coordinación multiagente, con tabla de selección rápida y pautas de evolución.

## Fuente
- https://claude.com/blog/multi-agent-coordination-patterns
