[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta la “estrategia de asesor” (advisor strategy): combinar un modelo más potente (Opus) como asesor con un modelo más económico (Sonnet o Haiku) como ejecutor, para obtener orientación de alta calidad cuando hace falta sin pagar el coste del modelo más caro en todo momento.

## ¿Cuándo es útil?
Es útil cuando tu flujo de trabajo con agentes puede avanzar de principio a fin usando herramientas casi siempre, pero en decisiones difíciles necesita razonamiento de mayor nivel solo de forma ocasional.

## Puntos clave
- El ejecutor (Sonnet/Haiku) realiza la tarea de extremo a extremo: llama herramientas, lee resultados e itera.
- Cuando lo necesita, el ejecutor consulta al asesor (Opus), que devuelve un plan/corrección/señal de parada, pero no llama herramientas ni genera salida final para el usuario.
- La “advisor tool” en Claude Platform lo convierte en un cambio pequeño en la solicitud de Messages API y mantiene el traspaso dentro de una sola petición.
- Puedes limitar las consultas con `max_uses`, y el uso del asesor se informa por separado.

## Recursos incluidos
- Una skill que documenta la estrategia de asesor e incluye el fragmento exacto de API del post: `skills/advisor-strategy-playbook/SKILL.md`.
- Un ejemplo ejecutable que contiene el fragmento de API: `skills/advisor-strategy-playbook/examples/messages_api_example.py`.

## Fuente
- https://claude.com/blog/the-advisor-strategy
