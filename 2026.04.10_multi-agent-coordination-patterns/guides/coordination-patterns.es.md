[English](./coordination-patterns.en.md) · [한국어](./coordination-patterns.ko.md) · **Español** · [日本語](./coordination-patterns.ja.md)

# Patrones de coordinación multiagente: guía de selección

## ¿De qué trata esta guía?
Una guía breve para seleccionar y evolucionar entre cinco patrones de coordinación multiagente descritos en el post.

## ¿Cuándo es útil?
Úsala cuando ya decidiste que necesitas múltiples agentes y ahora debes escoger una arquitectura que encaje con la estructura del trabajo y las restricciones operativas.

## Tabla rápida de selección

| Situación | Patrón |
| --- | --- |
| Salida crítica de calidad con criterios de evaluación explícitos | Generator-verifier |
| Descomposición clara con subtareas acotadas | Orchestrator-subagent |
| Subtareas paralelas, independientes y de larga duración | Agent teams |
| Pipeline basado en eventos, ecosistema de agentes en crecimiento | Message bus |
| Trabajo colaborativo donde los agentes construyen sobre hallazgos compartidos | Shared state |
| Evitar un único punto de falla | Shared state |

## Cómo evolucionar
- Empieza con el patrón más simple que pueda funcionar.
- Observa el modo de fallo principal.
- Evoluciona solo cuando el fallo sea persistente y estructural.

## Fuente
- https://claude.com/blog/multi-agent-coordination-patterns
