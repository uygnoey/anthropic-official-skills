[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post explica cómo el equipo de Claude Code diseña e itera herramientas para agentes pensando desde la perspectiva del modelo: “ver como un agente”.

## ¿Cuándo es útil?
Es útil cuando estás construyendo herramientas para agentes (o una plataforma de agentes) y necesitas decidir si añadir una herramienta nueva, cómo definir su interfaz y cómo evitar abrumar al modelo con demasiadas opciones.

## Puntos clave
- Las interfaces deben alinearse con las capacidades actuales del modelo; hay que revisar supuestos a medida que el modelo evoluciona.
- Añadir herramientas tiene un coste: más opciones aumentan la carga de decisión.
- Prioriza la divulgación progresiva y documentación reutilizable de “skills” en lugar de crear herramientas demasiado específicas.
- Si una herramienta se convierte en un cuello de botella, sustitúyela por un primitivo más expresivo (p. ej., pasar de “todos” a una abstracción de “tasks”).
- Para aclaraciones al usuario, una herramienta dedicada a preguntar puede ser más fiable que sobrecargar otra herramienta.

## Recursos incluidos
- Skill: heurísticas para diseñar interfaces de herramientas, divulgación progresiva y criterios estrictos para añadir nuevas herramientas.

## Fuente
- https://claude.com/blog/seeing-like-an-agent
