[English](./evaluating-frontier-coding-models.en.md) · [한국어](./evaluating-frontier-coding-models.ko.md) · **Español** · [日本語](./evaluating-frontier-coding-models.ja.md)

# Cómo evalúa Cursor los modelos de programación de frontera

Cursor es un agente de programación con IA para construir software profesional. Da soporte a todos los
grandes modelos de frontera junto al suyo propio, lo que convierte a la empresa en un juez
inusualmente neutral de cómo rinde cada uno en la práctica.

Nate Schmidt es el ingeniero que mantiene ese marcador. Trabaja en evaluaciones y comportamiento de
modelos en Cursor: estudia cómo aciertan los modelos, cómo fallan y qué hace que un desarrollador
abandone uno en silencio a mitad de una tarea. Cuando colegas y clientes quieren una lectura sobre un
lanzamiento nuevo, acuden a él.

## Por qué construyeron su propio benchmark

Con el tiempo, el equipo de Schmidt notó que las puntuaciones de los benchmarks públicos y la
recepción real de los desarrolladores habían dejado de coincidir. Así que construyeron el suyo:
CursorBench, una evaluación interna diseñada para capturar las formas desordenadas y poco
especificadas en que los ingenieros realmente escriben sus prompts.

> "Muchas evaluaciones tienen esta pinta: aquí hay un problema bien definido, aquí están las
> restricciones, ve y arréglalo. Pero los prompts que recibimos de usuarios reales no son así. El
> modelo tiene que inferir que el usuario tiene un problema y qué está tratando de transmitir,
> identificar la causa raíz, arreglarla, validar el arreglo e informar de vuelta."

Dos de sus tareas muestran lo que eso significa. Una consiste solo en un stack trace pegado con la
única palabra "fix": el modelo tiene que inferir la intención, encontrar la causa raíz y validar el
cambio por su cuenta. Otra le dice al modelo que el módulo equivocado está roto, para ver si cuestiona
la suposición del usuario o lo sigue hasta un callejón sin salida.

Lo que se puntúa no es el diff. Como lo plantea el artículo: la respuesta correcta es el mínimo
exigible; lo que puntúan es si el modelo entendió lo que se le estaba pidiendo.

## Verifica una puntuación sorprendente leyendo las trazas

Claude Fable 5 obtuvo un 72,9 % en el ajuste de Max effort de CursorBench, marcando un nuevo máximo.
La primera reacción del equipo de Cursor no fue celebrarlo.

> "Está pasando una de dos cosas: o el modelo es muy inteligente, o el modelo está haciendo trampa."

Así que leyeron las trazas: el razonamiento real del modelo en las tareas más difíciles, aquellas
donde el prompt parece simple pero resolverlo exige entender el sistema entero.

> "Seguíamos viendo al modelo desenterrar victorias que ningún otro modelo había logrado antes."

Además llegaba allí con menos operaciones: eficiente en tokens en relación con el trabajo completado.

La práctica transferible es la comprobación en sí. Un número que no has investigado todavía no es un
resultado, y la forma de investigarlo es leer cómo razonó realmente el modelo en las tareas que
separan a unos modelos de otros.

## Razonamiento local y razonamiento global

La segunda prueba de Schmidt era personal, no institucional: un simulador de vuelo espacial
programable y un prompt de una línea — construye un cohete y aterriza en la Luna.

Semanas antes lo había ejecutado con Claude Opus, dejándolo correr en un segundo monitor durante doce
a dieciséis horas. El modelo lanzaba, se quedaba sin combustible en órbita, añadía mucho más
combustible y luego no lograba salir de la atmósfera porque el cohete ya pesaba demasiado. Cada paso
de ese bucle es una respuesta localmente razonable al paso anterior.

Repitió el experimento con el mismo prompt en blanco, esta vez con Claude Fable 5. A los pocos
minutos, el cohete subió, se estacionó en órbita baja y volvió a bajar: aparentemente el mismo fallo.
Entonces leyó la transcripción.

> "Fable decidió que no iría a la Luna en su primer intento. Quería hacer una misión inicial solo para
> entrar en órbita y recoger telemetría, y luego usar eso para informar el siguiente viaje."

Unos intentos después, el ruido del motor se detuvo. Había un módulo posado en la Luna. La ejecución
completa llevó un par de horas, frente a las doce y pico de Opus sin resultado alguno.

> "Con Opus, hacía razonamiento local: pensaba en lo que acababa de pasar y en lo que estaba a punto de
> pasar. Con Fable es razonamiento global. Piensa en la misión entera."

Vale la pena notar qué habría ocurrido si solo se hubiera puntuado el resultado de la primera órbita:
dos fallos idénticos. La diferencia vivía en el plan.

## Cuándo apuntar al óptimo global

La regla de Schmidt para elegir modelo es lo bastante corta como para aplicarla sin deliberar:

> "Si tienes una buena idea de cómo es el camino de A a B, puede que no necesites Fable. Si estás en A
> y no tienes ni idea de dónde está B, Fable es una excelente elección. Cuando quiero construir algo
> de la manera correcta, Fable es el primer modelo en el que pienso."

De ahí se siguen tres consecuencias.

**El backlog cambia de categoría.** Fable ha permitido a su equipo retomar proyectos que habían
aparcado — reescrituras que todos coincidían en que serían mejores pero que nadie podía justificar en
semanas de trabajo — porque el modelo puede sostener buena parte del esqueleto. "Baja la energía de
activación para trabajar en este tipo de tareas. Nos permite movernos en busca de un óptimo global en
lugar de uno local."

**La coordinación se puede delegar.** Cursor funciona con estructura ligera, con una fuerte
responsabilidad individual y pocas reuniones de seguimiento. Antes de tocar código compartido, Schmidt
hace que un agente lea los commits recientes de su compañero y señale conflictos, de modo que ninguno
de los dos tenga que interrumpir lo que está haciendo para consultarlo.

**Mezcla modelos en vez de estandarizar en uno.** Para equilibrar coste y rendimiento, su equipo
combina Claude Fable 5 con modelos más rápidos y ligeros para el trabajo rutinario, y lo trae para los
problemas donde la capacidad es la restricción. En esa configuración, dice, la combinación es el
montaje más eficaz que han usado.

> "Si me meto en un problema realmente peliagudo — el p99 de los problemas — lo que intento optimizar
> es el tiempo hasta la solución. Y creo que Fable es el mejor modelo para resolver nuestros problemas
> más difíciles."

Schmidt también describe lo que dejó de tener que hacer: el cuidado constante — recordarle el contexto
al modelo, deletrearle la solución, auditar los resultados. "No siento que tenga que hacer un
bootstrap de Claude Fable 5 para que entienda el mundo en el que existo y el problema que intento
resolver. El modelo simplemente lo capta de fábrica."

## Qué viene después en Cursor

Schmidt sigue buscando los límites del modelo. A continuación quiere ver cuánto tiempo puede gestionar
un sistema de back-end sin supervisión; ejecuciones de días o semanas son su próximo experimento.
Dentro de Cursor, el equipo usa el modelo para cazar cuellos de botella de rendimiento y puntos de
fricción de los usuarios de forma proactiva en lugar de esperar a los informes, y para construir los
entornos de evaluación más sofisticados y cercanos a la realidad que medirán lo que venga después.

> "Hay una clase de problemas en los que la gente ni siquiera pensaba porque no parecían abordables.
> Con Fable, me entusiasma empujar en esa dirección."

## Fuente

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Blog de Claude, 17 de julio de 2026.
