[English](./opus-4-7-code-best-practices.en.md) · [한국어](./opus-4-7-code-best-practices.ko.md) · [Español](./opus-4-7-code-best-practices.es.md) · [日本語](./opus-4-7-code-best-practices.ja.md)

# Guía: Mejores prácticas para Opus 4.7 en Claude Code

Esta guía presenta las recomendaciones del artículo en forma de lista de verificación que puedes aplicar al configurar prompts y sesiones en Claude Code.

## Estructuración de sesiones interactivas
- Trata a Claude más como un ingeniero capaz al que delegas trabajo que como un programador en pareja al que guías línea por línea.
- Especifica la tarea desde el principio en el primer turno: intención, restricciones, criterios de aceptación y ubicación de archivos relevantes.
- Agrupa las preguntas y reduce las interacciones necesarias con el usuario para evitar sobrecarga innecesaria de razonamiento.
- Usa el modo auto cuando sea conveniente en tareas de larga duración donde confíes en que el modelo puede ejecutar con seguridad y con menos revisiones intermedias.

## Guía de niveles de esfuerzo
- `xhigh` es el nivel de esfuerzo predeterminado de Opus 4.7 en Claude Code y se sitúa entre `high` y `max`.
- Usa `high` cuando quieras reducir costos o estés ejecutando sesiones simultáneas.
- Usa `max` de forma deliberada para problemas genuinamente difíciles; ten en cuenta que los retornos disminuyen y aumenta la probabilidad de sobreanálisis.

## Prompts para el pensamiento adaptativo
- Opus 4.7 utiliza pensamiento adaptativo en lugar de Extended Thinking con un presupuesto de razonamiento fijo.
- Para fomentar más razonamiento, solicita un análisis cuidadoso paso a paso antes de responder.
- Para reducir el razonamiento, pide al modelo que priorice respuestas rápidas y directas cuando tenga dudas.

## Cambios de comportamiento a tener en cuenta
- La longitud de las respuestas se calibra según la complejidad de la tarea; si necesitas un estilo o extensión específicos, indícalo explícitamente.
- El modelo llama a las herramientas con menos frecuencia y razona más; describe explícitamente cuándo y por qué usar herramientas si deseas mayor uso de ellas.
- Por defecto genera menos subagentes; solicita explícitamente subagentes en paralelo cuando necesites distribuir trabajo entre archivos o elementos independientes.

## Fuente
- Best practices for using Claude Opus 4.7 with Claude Code (2026-04-16): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
