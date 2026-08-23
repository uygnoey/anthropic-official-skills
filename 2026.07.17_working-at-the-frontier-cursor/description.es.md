[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Nate Schmidt evalúa modelos de frontera en Cursor, un agente de programación con IA que da soporte a todos los grandes modelos de frontera junto al suyo propio, lo que convierte a la empresa en un juez inusualmente neutral del rendimiento de cada uno. Este post es su relato de cómo decidió que Claude Fable 5 estaba listo para los problemas más difíciles, y de qué cambió una vez que lo estuvo.

Dos hilos sostienen la historia. El primero es CursorBench, la evaluación interna que Cursor construyó cuando las puntuaciones de los benchmarks públicos y la recepción real de los desarrolladores dejaron de coincidir, diseñada alrededor de prompts poco especificados en lugar de problemas bien definidos. El segundo es la distinción que traza Schmidt entre el razonamiento local, que piensa en el paso recién dado y en el que viene, y el razonamiento global, que piensa en la misión entera.

## ¿Cuándo es útil?
- Cuando las puntuaciones de los benchmarks públicos ya no predicen cómo responden tus desarrolladores a un modelo.
- Cuando diseñas una evaluación interna y decides qué forma deben tener sus tareas.
- Cuando un resultado de benchmark da un salto y necesitas una forma de comprobar si creértelo.
- Cuando eliges entre un modelo de frontera y uno más barato para una tarea concreta.
- Cuando configuras un montaje con varios modelos y necesitas una regla sobre qué va a dónde.
- Cuando decides si una reescritura largamente aparcada merece empezarse ahora.

## Puntos clave
- **CursorBench nació porque las puntuaciones y la recepción divergieron.** Captura las formas desordenadas y poco especificadas en que los ingenieros escriben sus prompts: una tarea es un stack trace pegado con la única palabra "fix"; otra le dice al modelo que el módulo equivocado está roto, para ver si cuestiona la suposición o la sigue hasta un callejón sin salida.
- **Lo que se ejercita es la cadena completa.** "El modelo tiene que inferir que el usuario tiene un problema y qué está tratando de transmitir, identificar la causa raíz, arreglarla, validar el arreglo e informar de vuelta."
- **La respuesta correcta es el mínimo exigible.** Lo que Cursor puntúa es si el modelo entendió lo que se le estaba pidiendo.
- **72,9 % en Max effort** en CursorBench, un nuevo máximo — y la primera reacción del equipo fue la sospecha: "o el modelo es muy inteligente, o el modelo está haciendo trampa".
- **La comprobación consiste en leer las trazas.** En las tareas más difíciles, "seguíamos viendo al modelo desenterrar victorias que ningún otro modelo había logrado antes", y con menos operaciones: eficiente en tokens respecto al trabajo completado.
- **La prueba de la Luna.** Un modelo anterior corrió de doce a dieciséis horas en un simulador de vuelo espacial sin aterrizar, en un bucle entre quedarse sin combustible y pesar demasiado para despegar. Fable 5 planificó primero una misión orbital de telemetría y la usó para informar el aterrizaje; toda la ejecución llevó un par de horas.
- **Razonamiento local frente a global.** "Con Opus, hacía razonamiento local… Con Fable es razonamiento global. Piensa en la misión entera."
- **La regla de enrutado A-a-B.** "Si tienes una buena idea de cómo es el camino de A a B, puede que no necesites Fable. Si estás en A y no tienes ni idea de dónde está B, Fable es una excelente elección."
- **El trabajo aparcado cambia de categoría.** Reescrituras que nadie podía justificar en semanas se volvieron viables: "Baja la energía de activación… Nos permite movernos en busca de un óptimo global en lugar de uno local."
- **Combina modelos en vez de estandarizar.** El modelo de frontera para los problemas limitados por capacidad, modelos más rápidos y ligeros para el trabajo rutinario: el montaje más eficaz que ha usado el equipo.
- **Los agentes eliminan la sobrecarga de coordinación.** Antes de tocar código compartido, un agente lee los commits recientes de un compañero y señala conflictos, para que ninguno tenga que interrumpir al otro.
- **Lo siguiente:** ejecuciones sin supervisión de días o semanas sobre un sistema de back-end, caza proactiva de cuellos de botella de rendimiento y entornos de evaluación más cercanos a la realidad.

## Recursos incluidos
- `skills/frontier-model-routing/SKILL.md` — aplica la regla A-a-B, ejecuta un montaje mixto, optimiza el p99 por tiempo hasta la solución y revisa el backlog.
- `skills/frontier-model-routing/references/routing-heuristics.md` — las señales que empujan una tarea hacia cada modelo, y lo que el post deja sin especificar.
- `skills/frontier-model-routing/examples/routing-decisions.md` — el alunizaje, la reescritura aparcada y el agente de conflictos de commits, paso a paso.
- `skills/realistic-agent-evals/SKILL.md` — saca las tareas de prompts reales, incluye premisas falsas, puntúa la comprensión y lee las trazas cuando una puntuación se mueve.
- `skills/realistic-agent-evals/references/benchmark-design.md` — todo lo que el post afirma sobre cómo está construido CursorBench, y dónde se detiene.
- `skills/realistic-agent-evals/templates/eval-task-template.md` — plantillas para las tres formas de tarea, más un registro de resultado que lleva el ajuste de effort.
- `skills/realistic-agent-evals/examples/eval-tasks.md` — las dos tareas nombradas en el post, más ilustraciones completas de cada forma.
- `guides/evaluating-frontier-coding-models.{en,ko,es,ja}.md` — el relato completo en cuatro idiomas.

## Fuente
[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Blog de Claude, 17 de julio de 2026.
