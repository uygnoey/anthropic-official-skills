[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Base44 es una plataforma de *vibe coding* que permite a cualquiera, sin importar su nivel técnico, construir aplicaciones full stack y sitios web; sus clientes van desde pequeños negocios sin desarrolladores hasta compañías que crean productos SaaS completos. Yoav Orlev, su primer empleado y hoy responsable de producto, cuenta qué cambió cuando por fin se pudo confiar a un modelo el trabajo que estaba reservado a los ingenieros más senior de la compañía.

El artículo tiene dos hilos. El primero es la práctica de evaluación de Base44: cada nuevo modelo de Claude pasa por evaluaciones en distintos tipos de app midiendo latencia, coste y errores de compilación, más pruebas de estrés como construir un clon de Minecraft para ver cómo maneja la física y las mecánicas de juego. El segundo es el nivel de trabajo que se abrió cuando Claude Fable 5 superó esas evaluaciones: reconstruir un system prompt con cientos de permutaciones, arreglar el arnés que hay detrás del agente integrado y un product manager levantando por su cuenta la creación de apps móviles nativas.

## ¿Cuándo es útil?
- Cuando un cambio en el núcleo que toca partes interdependientes está en cola detrás de uno o dos ingenieros concretos.
- Cuando se diseña una suite de evaluación para un producto de generación de código o de apps.
- Cuando una evaluación pasa pero el coste en producción empeora igualmente, por ejemplo porque un cambio de prompt rompió la caché.
- Cuando se calibra cuánta especificación necesita realmente un modelo antes de una ejecución larga sin supervisión.
- Cuando se decide si alguien que no es ingeniero puede hacerse cargo de un trabajo técnico.
- Cuando una puerta de revisión-prueba-aprobación debe sustituir a la supervisión paso a paso.

## Puntos clave
- **El cuello de botella era el radio de impacto, no la dificultad.** Las funcionalidades de alcance pequeño y medio siempre avanzaron rápido; solo los cambios en el núcleo que tocan varias partes interdependientes quedaban reservados a los ingenieros más senior.
- **Dos cuellos de botella nombrados:** el system prompt y sus cientos de permutaciones (primera app o quinta, usuario gratuito o suscriptor, categoría y funcionalidades de la app), y la infraestructura móvil nativa, que solo podían cambiar ingenieros con experiencia en móvil.
- **El comportamiento que descartaba a los modelos anteriores:** al atascarse con un error, seguían trabajando el punto que tenían delante en lugar de reconocer que la solución probablemente ya existía en otra parte del código y buscarla. "La decisión sobre qué hacer a continuación es crucial, y la mayoría de las veces los modelos [anteriores] adoptaban, diría yo, un enfoque ingenuo". — Yoav Orlev
- **Claude Fable 5 fue el primer modelo que el equipo probó capaz de razonar como si entendiera cómo se construye el software.**
- **La suite de evaluación:** evaluaciones en distintos tipos de app midiendo latencia, coste y errores de compilación, más pruebas de estrés como un clon de Minecraft para física y mecánicas de juego.
- **Dos cosas destacaron:** muchos menos turnos hasta completar la tarea y apps más completas desde el primer prompt, incluidos los casos límite que los modelos anteriores se saltaban.
- **La reconstrucción del system prompt:** alrededor de una hora de preguntas y respuestas, luego cuatro horas por su cuenta, devolviendo entre el 90% y el 95% de lo necesario; medido y desplegado con la infraestructura de tests A/B esa misma tarde.
- **El modelo encontró una laguna en las propias evaluaciones de Base44:** no se probaban los aciertos de caché, pese a que un cambio de prompt puede romperla y, a escala de millones de usuarios, eso dispara el coste.
- **El arreglo en el arnés:** atascado con un cambio en el arnés del agente integrado, razonó que el problema probablemente ya se había resuelto en otro sitio, fue a investigar y volvió con la solución. "Este razonamiento de 'esto probablemente ya se ha resuelto en otro sitio, así que debería ir allí a investigar' es algo que no hemos visto tan a menudo en otros modelos".
- **Informa del objetivo y del porqué.** Orlev lo compara con un ingeniero senior: a un júnior hay que especificarle cada paso y revisarlo constantemente; a un senior le basta el objetivo y el porqué.
- **Un product manager hizo el trabajo de móvil nativo:** unas dos horas y media hasta un entorno funcional que cubría alrededor del 90% de lo necesario para producción.
- **La revisión pasó a ser la puerta, y la supervisión dejó de ser el método.** El modelo ejecuta; el equipo revisa, prueba y aprueba antes de desplegar.
- **Qué viene después:** convertir Base44 de una herramienta que construye apps en una que ayuda a gestionarlas y hacerlas crecer, con Base44 Superagents ya público. "Fable nos ha dado la confianza para hacer movimientos más audaces con el negocio".

## Recursos incluidos
- `skills/app-generation-model-evals/SKILL.md` — evaluar en distintos tipos de app, añadir pruebas de estrés, puntuar turnos y completitud desde el primer prompt, probar aciertos de caché y desplegar tras medición A/B.
- `skills/app-generation-model-evals/references/eval-dimensions.md` — cada dimensión, por qué importa el abanico de tipos de app y lo que el artículo no especifica.
- `skills/app-generation-model-evals/templates/model-eval-run.md` — un registro de ejecución comparable por modelo, incluyendo caché y casos límite.
- `skills/app-generation-model-evals/examples/fable-5-evaluation.md` — la ejecución de Fable 5 con sus cifras y una tabla de antes y después.
- `skills/senior-scope-delegation/SKILL.md` — identificar el trabajo en cola detrás de personas, comprobar el razonamiento sobre dónde trabajar, informar del objetivo y el porqué, adelantar las preguntas y poner la revisión como puerta.
- `skills/senior-scope-delegation/references/review-gate.md` — qué sustituyó el revisar-probar-aprobar y qué hace defendible desplegar el mismo día.
- `skills/senior-scope-delegation/templates/goal-and-why-brief.md` — un brief que enuncia el resultado y la restricción en lugar de los pasos.
- `skills/senior-scope-delegation/examples/base44-handoffs.md` — las tres entregas, el cuello de botella que despejaron y lo que Base44 construye a continuación.
- `guides/trusting-a-model-with-core-changes.{en,ko,es,ja}.md` — el relato completo en cuatro idiomas.

## Fuente
[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Blog de Claude, 15 de julio de 2026.
