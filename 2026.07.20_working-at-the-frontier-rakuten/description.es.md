[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Yusuke Kaji, director general de IA para Negocio en Rakuten, lleva probando modelos de Claude desde septiembre de 2024 —a lo largo de casi una docena de lanzamientos— y describe Claude Fable 5 como un salto cualitativo para los agentes empresariales de larga duración. Su trabajo consiste en "encontrar las semillas de la innovación transformadora y escalarlas por toda la compañía", y una de esas semillas fue Claude.

El artículo tiene dos hilos. El primero es el esfuerzo corporativo que Rakuten llama AI-nization: desde marzo de 2025, Claude Code acelerando el desarrollo de software, agentes desplegados en producto, ventas, marketing y finanzas en menos de una semana desde la llegada de los Claude Managed Agents, y funciones de IA al servicio de millones de clientes. El segundo es por qué antes fallaban las ejecuciones largas sin supervisión y ya no fallan: el modelo revisa su propio trabajo sobre la marcha, lo que permite a Kaji entregar una tarea entera en lugar de trocearla, ejecutar varias a la vez y dormir mientras un trabajo termina de noche.

## ¿Cuándo es útil?
- Cuando un agente debe ejecutarse cinco horas o una jornada entera sin que nadie revise.
- Cuando una ejecución larga falla una y otra vez porque una suposición equivocada temprana se acumuló sin ser detectada.
- Cuando hay que decidir qué tamaño de unidad de trabajo entregar a un agente: un bloque bien definido o la tarea completa.
- Cuando el número de tareas que asume la organización crece más rápido que el juicio disponible para revisarlas.
- Cuando el precio de frontera limita hasta dónde se puede desplegar un modelo y hay que enrutar el trabajo.
- Cuando se prepara un conjunto permanente de tareas difíciles para apuntar a cada modelo nuevo.

## Puntos clave
- **La autoverificación es lo que hace viable una ejecución sin supervisión.** "Probamos Fable y nos encanta su capacidad de autorreflexión y autoverificación. Comparado con los modelos anteriores, entiende su error antes de que yo se lo señale a las dos o las tres de la madrugada, así que puedo dormir". — Yusuke Kaji
- **El modo de fallo anterior no era el primer paso equivocado, sino que nada lo detectaba.** "Si eligen el camino correcto en el primer paso, todo va bien. Pero si eligen la dirección equivocada en la primera pasada, el agente dedica un tiempo considerable a corregir el rumbo, o incluso no llega a su destino".
- **Tres comportamientos marcan el salto:** revisa de nuevo sus propias suposiciones cuando el estado de la tarea cambia a mitad de camino; vuelve a los primeros principios en cada paso, revalidando contra la intención original sin que se lo pidan; y su juicio en decisiones ambiguas coincide con el del equipo.
- **Alineación de criterio** (*taste alignment*) es el término que acuñó Kaji para ese tercer comportamiento: "más fluida con Fable que con cualquier modelo anterior de vuestra compañía, o cualquier otro modelo que hayamos usado".
- **La unidad de trabajo subió.** "Antes de Fable teníamos que dividir el trabajo en bloques bien definidos para que el agente los ejecutara". Ahora entrega una tarea entera y ejecuta varias a la vez.
- **La aprobación final se volvió viable,** y la unidad de trabajo que maneja Kaji pasa de la tarea a la decisión.
- **Los agentes conservan memoria entre ejecuciones:** "Nuestros agentes con memoria recuerdan qué salió mal en sesiones pasadas y evitan repetir esos errores".
- **AI-nization avanzó rápido:** agentes desplegados en producto, ventas, marketing y finanzas en menos de una semana, conectados a Slack, Microsoft Teams y el sistema de tareas propio de Rakuten.
- **La restricción se movió dos veces:** de quién sabía escribir código, a quién entiende el problema de negocio, al juicio humano. Los agentes cierran incidencias unas 10 veces más rápido, pero añadir más agentes no añade juicio.
- **El enrutamiento por coste es explícito:** medir la tasa de finalización junto con el coste por tarea, enviar a Fable 5 el trabajo donde la capacidad adicional cambia el resultado y dejar el resto a modelos más pequeños. Dos cosas inclinan la cuenta: menos tokens y menos giros equivocados, y menos acompañamiento.
- **Las tareas de estiramiento se preparan a propósito.** "Igual que un buen líder prepara objetivos ambiciosos para su gente, nosotros preparamos tareas ambiciosas para un Claude nuevo".
- **Lo siguiente es la coordinación, no la velocidad:** agentes que "coordinen u organicen, más como un mánager", sosteniendo el matiz que suele perderse entre los miembros de un equipo.

## Recursos incluidos
- `skills/overnight-agent-delegation/SKILL.md` — entregar la tarea entera, comprobar los tres comportamientos de autoverificación, dar memoria a los agentes y esperar que el juicio se convierta en la restricción.
- `skills/overnight-agent-delegation/references/self-verification-behaviors.md` — cada comportamiento tal como lo enuncia el artículo, y lo que deja sin especificar.
- `skills/overnight-agent-delegation/templates/stretch-task-brief.md` — un brief reutilizable para la tarea de estiramiento a la que se apunta un modelo nuevo.
- `skills/overnight-agent-delegation/examples/rakuten-agent-runs.md` — la ejecución nocturna, el despliegue de AI-nization y la restricción que sustituyó a escribir código.
- `skills/intelligence-cost-routing/SKILL.md` — medir juntas la tasa de finalización y el coste por tarea, y enrutar según si la capacidad adicional cambia el resultado.
- `skills/intelligence-cost-routing/references/cost-signals.md` — cómo la autoverificación se convierte en una propiedad de coste, y lo que el artículo no especifica.
- `skills/intelligence-cost-routing/templates/task-routing-record.md` — un registro de enrutamiento por clase de tarea con bitácora de reevaluación.
- `guides/building-an-ai-native-workforce.{en,ko,es,ja}.md` — el relato completo en cuatro idiomas.

## Fuente
[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Blog de Claude, 20 de julio de 2026.
