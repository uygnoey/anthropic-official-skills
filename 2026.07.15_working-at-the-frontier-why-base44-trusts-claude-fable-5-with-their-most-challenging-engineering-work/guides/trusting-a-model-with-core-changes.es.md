[English](./trusting-a-model-with-core-changes.en.md) · [한국어](./trusting-a-model-with-core-changes.ko.md) · **Español** · [日本語](./trusting-a-model-with-core-changes.ja.md)

# Confiar cambios en el núcleo a un modelo: el relato de Base44

Base44 es una plataforma de *vibe coding* que permite a cualquiera, sin importar su nivel técnico,
construir aplicaciones full stack y sitios web. Sus clientes van desde pequeños negocios sin
desarrolladores hasta compañías que la usan para crear productos SaaS completos. Esta guía sigue el
relato tal como lo cuenta el artículo.

## La plataforma y la misión

Yoav Orlev entró en Base44 como su primer empleado y hoy dirige producto. Dice que una de las partes más
satisfactorias de su trabajo es ver lo que los pequeños negocios logran con la plataforma cuando antes
les faltaba tiempo, presupuesto o conocimiento: montar una tienda digital o una aplicación de gestión de
turnos para el personal de un restaurante. La misión de su equipo es seguir ampliando las capacidades del
producto sin dejar de hacerlo usable para todo el mundo.

## El cuello de botella: cambios en el núcleo que tocan partes interdependientes

Los equipos de producto e ingeniería de Base44 siempre se han movido rápido, sobre todo al lanzar
funcionalidades de alcance pequeño o medio. Pero cualquier cambio en el núcleo de la plataforma que
tocara múltiples partes interdependientes solo podía confiarse a los ingenieros más senior.

Dos de esos cuellos de botella:

- **El system prompt y sus cientos de permutaciones,** que varían según si alguien está en su primera
  app o en la quinta, si es usuario gratuito o suscriptor, y según la categoría y las funcionalidades de
  la app que se está construyendo.
- **La infraestructura móvil nativa,** que solo podían cambiar ingenieros con experiencia en móvil.

## Por qué no se podía confiar en los modelos anteriores

Los modelos de Claude han alimentado el motor de generación de apps de Base44 desde su lanzamiento a
principios de 2025, pero no se les podía confiar ese nivel de trabajo, sugiere Orlev. Cuando un modelo se
atascaba con un error, por ejemplo, seguía trabajando el punto que tenía delante en lugar de reconocer
que la solución probablemente ya existía en otra parte del código y buscarla.

> "La decisión sobre qué hacer a continuación es crucial, y la mayoría de las veces los modelos
> [anteriores] adoptaban, diría yo, un enfoque ingenuo".

Claude Fable 5 fue el primer modelo que el equipo probó capaz de razonar como si entendiera cómo se
construye el software, dice Orlev.

## Cómo evalúa Base44 un modelo nuevo

Base44 pasa cada nuevo modelo de Claude por evaluaciones en distintos tipos de app, midiendo
**latencia**, **coste** y **errores de compilación**. El equipo también ejecuta pruebas como construir un
**clon de Minecraft** para ver cómo maneja el modelo la física y las mecánicas de juego.

Con Claude Fable 5 destacaron dos cosas:

- Terminaba las tareas en **muchos menos turnos**.
- Construía **apps más completas desde el primer prompt**, incluidos los casos límite que los modelos
  anteriores se saltaban.

## La reconstrucción del system prompt

Así que el equipo lo apuntó a una tarea que antes reservaban solo a los ingenieros más senior:
reconstruir el system prompt de Base44.

Tras aproximadamente **una hora** de preguntas y respuestas, Claude Fable 5 trabajó por su cuenta durante
**cuatro horas** y devolvió entre el **90% y el 95%** de lo que necesitaban. Con su infraestructura de
tests A/B, el equipo pudo medir y desplegar esos cambios **esa misma tarde**.

Y mientras trabajaba, Claude Fable 5 incluso señaló una laguna en las propias evaluaciones de Base44: el
equipo no estaba probando los **aciertos de caché**, pese a que un cambio de prompt puede romper la caché
y, a escala de millones de usuarios, eso dispara el coste. El modelo sacó a la luz un punto ciego y lo
corrigió.

## El arreglo en el arnés

Cuando Claude Fable 5 se atascó con un cambio en el arnés que hay detrás del agente integrado de Base44,
razonó que el mismo problema probablemente ya se había resuelto en otra parte del código, fue a
investigar esa zona y volvió con la solución.

> "Este razonamiento de 'esto probablemente ya se ha resuelto en otro sitio, así que debería ir allí a
> investigar' es algo que no hemos visto tan a menudo en otros modelos".

## Informar como a un ingeniero senior

Orlev compara trabajar con Claude Fable 5 con trabajar con un ingeniero senior. Mientras que a un
ingeniero júnior hay que especificarle cada paso y revisarlo constantemente, a uno senior solo hace falta
explicarle el objetivo y el porqué.

## Más allá de ingeniería

Este tipo de trabajo se extiende también fuera del equipo de ingeniería. Cuando un **product manager**
quiso incorporar la creación de apps móviles nativas dentro de Base44, apuntó Claude Fable 5 al encargo y
tras unas **dos horas y media** tenía un entorno funcional que cubría alrededor del **90%** de lo que el
equipo necesitaba para pasar a producción.

Antes de Claude Fable 5, este tipo de trabajo tenía que esperar a que se liberaran los tres mejores
ingenieros de Base44 o un especialista. Ahora el modelo ejecuta las tareas mientras el equipo de Orlev
**revisa, prueba y aprueba** el código antes de desplegarlo.

## Qué viene después

A medida que avanzan las capacidades de los modelos de Claude, avanzan también los objetivos del equipo
de Base44 para la plataforma. El equipo quiere convertir Base44 de una herramienta que construye apps en
una que además ayude a gestionar y hacer crecer lo construido. **Base44 Superagents**, ya público,
ejecuta flujos de trabajo alrededor de esas apps.

Sabiendo que pueden confiar tareas complejas a Fable 5, Orlev ahora anima a product managers y
diseñadores a construir en partes de la plataforma que antes no estaban dispuestos a tocar por miedo a
romper algo.

> "Fable nos ha dado la confianza para hacer movimientos más audaces con el negocio. Está llevando el
> producto a un terreno completamente nuevo y a posibilidades que antes, diría yo, nos daban miedo".

## Fuente

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Blog de Claude, 15 de julio de 2026.
