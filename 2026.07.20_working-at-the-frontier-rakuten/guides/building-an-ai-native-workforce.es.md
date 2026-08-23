[English](./building-an-ai-native-workforce.en.md) · [한국어](./building-an-ai-native-workforce.ko.md) · **Español** · [日本語](./building-an-ai-native-workforce.ja.md)

# Construir una plantilla nativa de IA: el relato de Rakuten

Yusuke Kaji, director general de IA para Negocio en Rakuten, lleva probando modelos de Claude desde
septiembre de 2024. Su trabajo consiste en "encontrar las semillas de la innovación transformadora y
escalarlas por toda la compañía". Una de esas semillas fue Claude. Esta guía sigue el relato tal como lo
cuenta el artículo.

## El despliegue, en orden

Desde marzo de 2025, Rakuten ha usado Claude para acelerar el desarrollo de software con Claude Code,
poner en marcha agentes en sus áreas de negocio y alimentar funciones de IA para millones de clientes.
Rakuten eligió asociarse con Anthropic por su enfoque empresarial, su liderazgo y su criterio de
producto.

A lo largo de casi una docena de lanzamientos de modelos, el trabajo que Kaji puede delegar a un agente
no ha dejado de crecer: primero usar Claude Code para llevar software a producción y después construir
Claude Managed Agents a medida para equipos de toda la compañía.

Rakuten llama a ese esfuerzo corporativo **AI-nization**: impregnar de IA todo lo que hace para
clientes, socios de negocio y empleados. Cuando llegaron los Claude Managed Agents, Rakuten desplegó
agentes en producto, ventas, marketing y finanzas **en menos de una semana**, conectados a Slack,
Microsoft Teams y al propio sistema de tareas de la compañía.

## La restricción se movió

Para Kaji y su equipo, la restricción para construir agentes solía ser quién sabía escribir código.
Ahora es quién entiende el problema de negocio.

> "La corporación moderna está diseñada para minimizar el coste de la comunicación. Creo que agentes
> como Claude Code pueden brillar cuando trabajamos con ellos para minimizar también el coste de la
> nueva innovación, como una transición rápida de la idea a producción".

Dale a una persona capaz agentes que sostengan contexto y criterio, y "permite que el talento oculto
libere su potencial y lo escale cien veces más".

## Y volvió a moverse: hacia el juicio

Ejecutar agentes en todas las áreas las veinticuatro horas hace aflorar una nueva restricción: el juicio
humano.

Los agentes de Rakuten cierran incidencias unas **10 veces más rápido** en todos los dominios, y el
número de tareas que la organización asume no deja de subir. Añadir más agentes no añade juicio. Así que
cuanto más rápido corren los agentes, más depende el avance de la organización de que una persona cierre
el bucle.

## Por qué fallaban antes las ejecuciones largas

Para la mayoría de quienes construyen, lo más difícil de los agentes de larga duración es prepararlos
para que tengan éxito con una supervisión mínima. Conectarlos a las herramientas y al contexto adecuados
es una cosa, pero según la experiencia de Kaji siempre hubo límites a cuánto podía avanzar un agente sin
que una persona validara su trabajo.

> "Si eligen el camino correcto en el primer paso, todo va bien. Pero si eligen la dirección equivocada
> en la primera pasada, el agente dedica un tiempo considerable a corregir el rumbo, o incluso no llega
> a su destino".

En un trabajo pensado para durar cinco horas o una jornada entera, una sola suposición equivocada al
principio podía quemar la ejecución completa, y la única manera de detectarla era que alguien revisara.

El modo de fallo era la **ausencia de autoverificación**. Cualquier modelo puede dar un primer paso
equivocado. El problema de los modelos anteriores era que no revisaban su propio trabajo sobre la
marcha, así que un giro erróneo temprano pasaba inadvertido, se acumulaba durante la ejecución y
producía un resultado subóptimo horas después.

## Qué cambió con Claude Fable 5

Kaji afirma que Fable 5 cambia el cálculo de las ejecuciones agénticas de varios días porque revisa su
propio trabajo sobre la marcha, mucho más a menudo que cualquier modelo anterior.

> "Probamos Fable y nos encanta su capacidad de autorreflexión y autoverificación. Comparado con los
> modelos anteriores, entiende su error antes de que yo se lo señale a las dos o las tres de la
> madrugada, así que puedo dormir".

Su equipo señala tres comportamientos que marcan el salto:

- **Revisa de nuevo sus propias suposiciones.** Cuando el estado de la tarea cambia a mitad de camino,
  Fable 5 lo advierte y corrige una suposición equivocada antes de actuar sobre ella, en lugar de
  comprometerse con un mal camino y descubrirlo horas después.
- **Vuelve a los primeros principios en cada paso.** Revalida contra la intención original sin que se lo
  pidan: la corrección de rumbo que antes tenía que hacer Kaji en persona.
- **Encaja con el criterio del equipo.** Incluso con una guía mínima, su juicio en las decisiones ambiguas
  coincide con el suyo. Kaji acuñó un término para esto: *alineación de criterio* (*taste alignment*).
  "La alineación de criterio es más fluida con Fable que con cualquier modelo anterior de vuestra
  compañía, o cualquier otro modelo que hayamos usado".

## La unidad de trabajo cambió

> "Antes de Fable teníamos que dividir el trabajo en bloques bien definidos para que el agente los
> ejecutara".

Ahora Kaji entrega una tarea entera y ejecuta varias a la vez. El modelo reflexiona en cada paso, detecta
una mala suposición temprana y encuentra por sí mismo el camino de vuelta a los primeros principios,
renavegando hacia el resultado correcto sin que nadie lo dirija.

Como el modelo se autocorrige durante la ejecución, la aprobación final se vuelve viable por primera vez,
y la unidad de trabajo que Kaji delega pasa **de la tarea a la decisión**. Los agentes además conservan
memoria entre ejecuciones: "Nuestros agentes con memoria recuerdan qué salió mal en sesiones pasadas y
evitan repetir esos errores".

Como resultado, el número absoluto de tareas sigue subiendo, pero las que realmente necesitan a una
persona se mantienen en un nivel abarcable. No tener que intervenir para corregir el rumbo a mitad de
ejecución es, dice Kaji, la mayor ganancia de productividad de todas: permite a su equipo dedicar su
tiempo a las decisiones que solo deberían tomar las personas y mantiene a una organización nativa de IA
acelerando en lugar de atascarse en correcciones humanas de rumbo.

## Preparar tareas de estiramiento

Kaji compara probar un modelo nuevo con emprender una "nueva misión".

> "Igual que un buen líder prepara objetivos ambiciosos para su gente, nosotros preparamos tareas
> ambiciosas para un Claude nuevo. Quizá Claude también nos esté empujando a estirarnos".

## Equilibrar coste y eficiencia

La capacidad de frontera tiene un precio de frontera, y Kaji es directo: el coste decide hasta dónde
puede desplegar. "Como gran empresa, queremos equilibrar inteligencia y coste".

Su equipo mide la **tasa de finalización de tareas** junto con el **coste por tarea**, y luego envía a
Fable 5 el trabajo donde la capacidad adicional cambia el resultado, dejando el resto a modelos más
pequeños.

Dos cosas inclinan la cuenta a favor de Fable 5: hace más con menos tokens y menos giros equivocados, y
necesita menos acompañamiento.

## Qué viene después

La frontera que Kaji está probando ahora no es la velocidad individual. Es conseguir que los agentes
**coordinen a las personas**. Claude Code ha acelerado su trabajo y el de sus colegas, pero la parte
difícil de cualquier organización es la alineación entre personas: encajar el contexto y el criterio de
una con los de otra. Está explorando agentes que "coordinen u organicen, más como un mánager",
sosteniendo el matiz que suele perderse entre los miembros de un equipo.

> "No vemos a los agentes de IA como futuros colegas ni como competidores. Son sistemas a nuestro
> alrededor".

Y le aplica a Anthropic su propio consejo: construye para el modelo que llegará dentro de tres o seis
meses, no para el que tienes delante.

> "Creo que como sociedad todavía no hemos encontrado el encaje modelo-tarea para Claude Fable 5, pero ya
> destaca como un modelo que cruzó la línea y se pasó a nuestro mundo".

## Fuente

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Blog de Claude, 20 de julio de 2026.
