[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post explica cuándo los sistemas multiagente superan a un solo agente y cómo descomponer y verificar el trabajo de forma segura.

## ¿Cuándo es útil?
Es útil cuando un solo agente se degrada por contaminación de contexto, cuando necesitas exploración en paralelo o cuando la especialización mejora la fiabilidad.

## Puntos clave
- Empieza con un solo agente; los sistemas multiagente añaden sobrecarga y aumentan el coste en tokens.
- Úsalos principalmente para protección del contexto, paralelización y especialización.
- Prefiere una descomposición centrada en el contexto (límites de contexto, no “fases”).
- Usa un subagente de verificación con criterios explícitos para evitar la “victoria temprana”.

## Recursos incluidos
- Skill: multi-agent-decision-framework
- Ejemplos: protección de contexto, investigación en paralelo, enrutamiento por especialización, bucle de verificación

## Fuente
- https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
