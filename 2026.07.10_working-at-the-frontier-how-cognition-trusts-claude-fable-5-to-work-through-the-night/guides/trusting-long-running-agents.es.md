[English](./trusting-long-running-agents.en.md) · [한국어](./trusting-long-running-agents.ko.md) · **Español** · [日本語](./trusting-long-running-agents.ja.md)

# Cómo decide Cognition que un agente puede quedarse trabajando solo

Cognition es joven, incluso para los estándares de Silicon Valley. Construyó Devin, su ingeniero de
software autónomo con IA, a principios de 2024, cuando la mecánica básica de un agente apenas se
sostenía.

Devin asume el trabajo al que los ingenieros nunca llegan: migraciones de código, el atasco de bugs,
las funcionalidades que se van posponiendo. Con clientes que van desde startups en rápido crecimiento
hasta empresas Fortune 500, el listón está alto. El código que escribe Devin tiene que ser fiable y
listo para producción; un bug pequeño introducido en silencio puede causar problemas reales aguas
abajo.

Silas Alberti, SVP de Investigación, entrena y prueba los modelos que hay detrás de Devin, y ha usado
casi todas las generaciones de Claude desde el principio.

## "No nos fiamos de ninguna evaluación"

Alberti sitúa el primer salto real en Claude 3.6 Sonnet, a finales de 2024. Fue el primer modelo capaz
de encadenar herramientas de forma fiable y sostener una tarea de varios pasos. Cuando el equipo lo
conectó a Devin, el uso interno se triplicó.

Esa historia es lo que hace difícil impresionarle. Cognition ha visto modelos arrasar en un benchmark
y desmoronarse en cuanto sus ingenieros intentaban usarlos. "Nos hemos quemado así un montón de
veces", dice Alberti. Así que el equipo confía en sus propios ingenieros por encima de cualquier
puntuación: sus desarrolladores con mejor criterio someten cada modelo nuevo a un día real de trabajo,
y el listón es si el código es algo que de verdad se quedarían.

Como lo formula Alberti: "no nos fiamos de ninguna evaluación".

La regla trata de qué cuenta como evidencia, no de evitar medir: Cognition también mantiene su propio
benchmark.

## Dónde topaban los modelos anteriores

Pese a todo ese progreso, quedaba un techo: cuánto tiempo podía correr un agente antes de perder el
hilo.

> "Antes de Fable, podías delegar en agentes capaces de mantenerse en la tarea un par de minutos,
> quizá una hora."

Después de eso, las sesiones derivaban. Dale a un modelo anterior cinco ideas que sopesar a la vez y
se perdía y se confundía. En una migración de base de datos, un modelo Opus previo terminó
técnicamente el trabajo, pero introdujo por el camino una serie de bugs sutiles: el fallo caro,
precisamente porque informa de éxito.

El triaje de incidentes mostraba la misma forma. Los modelos anteriores tendían a quedarse en la
superficie de los logs en vez de excavar hasta la línea relevante, y estaban entrenados para dar una
respuesta pasara lo que pasara, así que "afirmaban con seguridad la primera cosa plausible que
descubrían y ahí paraban". Los ingenieros aprendieron a ignorarlos.

Esa última frase es el coste real. Un modelo cuya salida se ignora no aporta valor ni siquiera cuando
acierta.

## Superar el listón de la propia Cognition

Cognition califica los modelos con Frontier Code, un benchmark que construyó porque los existentes
seguían premiando código que pasaba los tests pero no sobreviviría en un codebase real. Alberti lo
llama un estándar "anti-slop".

En su subconjunto más difícil, el modelo Opus previo sacaba alrededor de un 10 %. Claude Fable 5 sacó
cerca del 30 %.

La primera reacción del equipo fue la sospecha. "¿Hay un bug? Esto no puede ser cierto." Normalmente
un salto en un benchmark viene acompañado de ingenieros discutiendo durante semanas si el modelo es
realmente mejor en la práctica. Esta vez el dogfooding coincidió con los números.

> "Fue un poco impactante, la verdad."

Una puntuación y un día de dogfooding que coinciden es un resultado mucho más fuerte que cualquiera de
los dos por separado. Y, según el propio artículo, esa coincidencia es la parte inusual.

## Lo que cambió: el horizonte

> "Lo más grande que notamos fue el horizonte, cuánto tiempo puede ser autosuficiente. Ha habido
> tareas en las que estaba a punto de irme a dormir y le dije: 'Vale, sigue trabajando en esto y no
> pares hasta que me despierte'. Y me despierto, y lleva ocho horas seguidas trabajando y haciendo
> progreso real. No había visto eso antes."

Ambas mitades importan. Ocho horas es el horizonte; *progreso real* es la parte que fallaba en las
ejecuciones largas anteriores, porque un agente puede mantenerse ocupado indefinidamente sin
mantenerse en la tarea.

El artículo da tres razones por las que el horizonte se sostuvo.

**Mantuvo la cabeza clara en contexto desordenado.** Fue el primer modelo en usar correctamente las
herramientas internas de depuración de Cognition, recorriendo logs en el navegador y sacando
conclusiones pese al ruido. Un agente que solo puede leer lo que le pegas está limitado a tu capacidad
de atención.

**Declaró sus invariantes antes de ejecutar.** En una migración que había hecho tropezar a modelos
anteriores, enunció las invariantes a las que se sujetaría y luego ejecutó contra ellas. En una
ejecución larga sin supervisión, las invariantes son lo que sustituye a tu vigilancia — y revisarlas
antes de empezar es mucho más barato que leer ocho horas de diff.

**Dijo lo que no sabía.** En el triaje, identificó la causa raíz y nombró los límites de lo que había
establecido, que es lo que según Alberti reconstruye la confianza de verdad. Una respuesta con un
límite declarado te dice qué parte verificar. Una respuesta segura sin límite te obliga a verificarlo
todo, que es lo mismo que hacer el triaje tú.

## Qué viene después

La apuesta fundacional de Cognition era que los agentes deberían correr en la nube durante horas. El
primer año de la empresa, los modelos no daban para eso.

Alberti dice que Claude Fable 5 hace viable la versión completa de esa apuesta, y parte ya está en el
producto. Devin puede vigilar un canal de Slack y meterse en un problema sin que le etiqueten, o
monitorizar producción y triar un pico por su cuenta. Cuando acierta con una de esas, dice, se siente
"como un ingeniero de verdad en el equipo".

Espera que esto se convierta en lo habitual para los equipos de ingeniería. En uno o dos años, dice,
el 90 % de las sesiones de agente serán proactivas: encuentran un problema, escanean el codebase y te
escriben con el arreglo.

> "Muchas de las cosas que siempre quisimos construir en la empresa ahora son posibles."

## Fuente

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Blog de Claude, 10 de julio de 2026.
