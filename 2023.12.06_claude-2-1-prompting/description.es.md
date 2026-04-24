[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post describe un pequeño ajuste de prompting para contexto largo en Claude 2.1 que mejora la precisión en tareas tipo “needle in a haystack”.

## ¿Cuándo es útil?
Cuando aportas un documento muy largo (hasta ~200K tokens) y necesitas que el modelo responda basándose en una frase concreta que puede estar fuera de lugar o haber sido insertada.

## Puntos clave
- Claude 2.1 ofrece una ventana de contexto de 200K tokens y buen rendimiento en recuperación de información.
- El modelo puede mostrarse reacio a responder basándose en una sola frase fuera de contexto.
- Pedir que la respuesta empiece con “Here is the most relevant sentence in the context:” mejora notablemente la precisión.

## Recursos incluidos
- Skill: long-context-needle-finding
- Plantilla de prompt: frase inicial para encontrar el “needle”

## Fuente
- https://claude.com/blog/claude-2-1-prompting
