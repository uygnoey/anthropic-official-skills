[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Josefina Albert, del equipo de Educación de Anthropic, explica cómo trabajar con Claude Fable 5 dentro de Claude Cowork —el sistema de IA agéntica de Anthropic para el trabajo del conocimiento— cuando la tarea es larga, compleja y asíncrona.

La premisa es que un modelo más capaz exige otra forma de trabajar. Cowork ya divide un encargo grande en partes que corren en paralelo, cada una con su propio subagente, y fija un plan al inicio contra el que va contrastando sus resultados. La ventaja de Fable 5 en tareas largas y de muchos pasos encaja justo con esa forma: en un trabajo como construir el presupuesto del año que viene a partir de las cifras reales de este, planifica el flujo antes de empezar y detecta una tasa de consumo mal leída durante la ejecución, antes de que el error se propague a todas las proyecciones posteriores. Trabajar con él se parece a trabajar con un colega capaz: explicas la situación, acordáis qué es un buen resultado y le dejas trabajar.

## ¿Cuándo es útil?
- Cuando un encargo en Cowork abarca decenas de pasos, o varios días, y cada paso se apoya en el anterior.
- Cuando dudas entre Sonnet 5, Opus y Fable 5, o sobre qué nivel de esfuerzo (effort) configurar.
- Cuando partes de una idea todavía sin forma y quieres un interlocutor con acceso a tus archivos y herramientas.
- Cuando sigues escribiendo prompts paso a paso para un trabajo en el que solo importa el resultado.
- Cuando una conversación larga consume más uso del que esperabas.
- Cuando las skills o los archivos de memoria escritos para un modelo anterior pueden estar limitando a uno nuevo.

## Puntos clave
- **Fable 5 no es el modelo por defecto en Cowork**: hay que seleccionarlo. Sonnet 5 es el predeterminado y sirve para tareas del día a día; Opus encaja en trabajo profundo con una forma clara; Fable 5 es para los proyectos más complejos o ambiguos, sobre todo los que usan varias herramientas y exigen una serie de juicios.
- **El esfuerzo afina la elección.** Un esfuerzo alto implica más planificación previa y más comprobaciones durante la ejecución. Con esfuerzo bajo, en las pruebas de Anthropic Fable 5 igualó o superó con frecuencia a los modelos anteriores en su nivel máximo.
- **Nuevos clasificadores redirigen a Claude Opus 4.8.** Las solicitudes que rozan la ciberseguridad o la biología y la química pueden activarlos; se avisa al usuario cuando ocurre y la conversación se queda en Opus hasta que abras una nueva. Están ajustados de forma conservadora, así que hay falsos positivos.
- **Basta con empezar con una idea.** Hacer una lluvia de ideas en Cowork le da al modelo tus archivos reales y tus herramientas conectadas como material de trabajo. Dos prompts: *«Antes de empezar, pregúntame todo lo que necesites saber para hacer esto bien»* y *«Esto es más o menos lo que quiero. Dame tres formas de abordarlo, con una muestra rápida de cada una»*.
- **El contexto vale más que las restricciones.** Una restricción solo dice qué no hacer; el contexto dice para qué es el trabajo, de modo que el modelo decide bien en situaciones que tus restricciones no anticiparon. Dale un borrador inicial y la versión final y deducirá tus estándares a partir de la diferencia.
- **Las conversaciones largas cuestan más.** Claude vuelve a leer toda la conversación con cada mensaje. Empieza las tareas nuevas en una conversación nueva y desactiva las tareas programadas que ya no necesites.
- **Delega el enfoque, el procedimiento o el calendario**: el método, qué skills se ejecutan o la periodicidad. Escribe tú los pasos solo cuando el proceso en sí importe.
- **El panel del plan es donde rediriges.** Enumera lo que Claude piensa hacer y luego los archivos y herramientas que usa. Un paso equivocado en el plan sale más barato de corregir que un resultado final equivocado: una frase lo arregla sin empezar de cero.
- **Invierte en la configuración:** conecta las herramientas que usas a diario, ajusta la escritura a tu voz (Fable 5 tiende a ser más escueto en sesiones largas) y audita las skills y la memoria escritas para modelos anteriores.

## Recursos incluidos
- `skills/delegating-complex-work-in-cowork/SKILL.md` — el método completo: elegir modelo y esfuerzo, arrancar desde una idea, informar con contexto, delegar la decisión, vigilar el plan e invertir en la configuración.
- `skills/delegating-complex-work-in-cowork/references/model-and-effort-selection.md` — la tabla de decisión de modelos, qué cambia el esfuerzo alto y bajo, y cómo funciona el repliegue a Opus 4.8.
- `skills/delegating-complex-work-in-cowork/references/setup-checklist.md` — conectar herramientas, ajustar la voz y revisar lo configurado para modelos anteriores.
- `skills/delegating-complex-work-in-cowork/templates/kickoff-prompts.md` — todos los prompts del artículo, agrupados por finalidad.
- `skills/delegating-complex-work-in-cowork/examples/delegation-patterns.md` — los tres patrones de delegación más los ejemplos del presupuesto y del panel de analítica desarrollados.
- `guides/working-with-a-frontier-model-in-cowork.{en,ko,es,ja}.md` — el recorrido completo en cuatro idiomas.

## Fuente
[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork) — Josefina Albert, 16 de julio de 2026.
