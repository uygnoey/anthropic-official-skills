[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## ¿De qué trata este post?
Explica cómo se comporta Opus 4.7 en Claude Code y cómo ajustar prompts y configuraciones (niveles de esfuerzo, pensamiento adaptativo, estructura de sesión) para mejorar calidad y eficiencia de tokens.

## ¿Cuándo es útil?
Es útil al actualizar de Opus 4.6 a 4.7 (o al configurar desde cero) y necesitas un comportamiento predecible, mejor uso de tokens y criterios para elegir niveles de esfuerzo.

## Puntos clave
- Aporta contexto desde el inicio: define intención, restricciones, criterios de aceptación y ubicaciones de archivos relevantes en el primer turno para reducir razonamiento adicional entre turnos.
- En sesiones interactivas, cada turno del usuario agrega sobrecarga de razonamiento; agrupa preguntas y reduce interacciones cuando sea posible.
- En Claude Code, el esfuerzo por defecto de Opus 4.7 es `xhigh` (entre `high` y `max`) y se recomienda para la mayoría del trabajo de codificación agentic; cambia el esfuerzo durante la tarea para equilibrar costo/latencia y rendimiento.
- Opus 4.7 usa pensamiento adaptativo (sin presupuesto fijo); puedes pedir explícitamente más o menos pensamiento según la necesidad.
- Cambios de comportamiento: la longitud de respuesta se ajusta a la complejidad, llama menos a herramientas y razona más, y genera menos subagentes por defecto—si necesitas más uso de herramientas o subagentes en paralelo, sé explícito.

## Recursos incluidos
- 1 skill (opus-4-7-code-best-practices)
- 1 guide set (opus-4-7-code-best-practices)

## Fuente
- Best practices for using Claude Opus 4.7 with Claude Code (2026-04-16): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
