[English](./session-management-1m-context.en.md) · [한국어](./session-management-1m-context.ko.md) · **Español** · [日本語](./session-management-1m-context.ja.md)

# Gestión de sesiones y ventana de contexto de 1M

Recorrido narrativo por la guía *Using Claude Code: session management and 1M context* (15 de abril de 2026).

## Por qué importa

El equipo de Claude Code lanzó el comando `/usage` y detectó un patrón consistente en sus conversaciones con clientes: los hábitos de uso varían muchísimo. Algunos desarrolladores mantienen una o dos terminales abiertas durante días; otros inician una nueva sesión en cada prompt. Con la nueva ventana de 1M tokens en Claude Code, estas decisiones importan más, no menos.

Casi toda la variación en resultados se reduce a **cómo gestionas la ventana de contexto**.

## Conceptos básicos

La ventana de contexto es todo lo que el modelo puede ver de una vez al generar su siguiente respuesta: system prompt, la conversación hasta ahora, cada llamada de herramienta con su salida y cada archivo leído. La ventana de Claude Code contiene un millón de tokens.

Pero el contexto tiene coste: el fenómeno del **context rot**. Cuando el contexto crece, la atención se reparte entre más tokens y el contenido antiguo e irrelevante empieza a distraer de la tarea actual. El rendimiento del modelo baja.

Cuando la ventana se acerca al límite, Claude Code resume la tarea en una descripción más corta y continúa en una nueva ventana. Esto es **compactación**. También puedes dispararla tú.

## Cada turno es un punto de ramificación

Tras la respuesta de Claude tienes cinco opciones:

- **Continue** — envía otro mensaje en la misma sesión.
- **`/rewind`** (o doble Esc) — salta a un mensaje anterior y vuelve a pedir desde ahí. Los mensajes posteriores se descartan.
- **`/clear`** — inicia una sesión nueva, normalmente con un brief destilado de lo que acabas de aprender.
- **`/compact`** — resume la sesión hasta ahora y continúa sobre ese resumen.
- **Subagentes** — delega el siguiente bloque a un agente con su propio contexto limpio y solo trae de vuelta su resultado.

Continuar es lo natural, pero las otras cuatro opciones existen para gestionar el contexto de forma deliberada.

## Cuándo iniciar una sesión nueva

Regla general: **tarea nueva ⇒ sesión nueva**. La ventana de 1M permite hacer tareas más largas con mayor fiabilidad — por ejemplo una app full-stack desde cero — pero el context rot sigue ocurriendo.

Hay excepciones. Escribir la documentación de una funcionalidad que acabas de implementar es técnicamente una tarea nueva, pero probablemente no quieras pagar por releer todos esos archivos. Mantén la sesión.

## Rebobinar en lugar de corregir

`/rewind` (doble Esc) te devuelve a cualquier mensaje anterior para volver a pedir desde ahí, descartando todo lo posterior.

Cuando Claude lee cinco archivos, intenta un enfoque y falla, lo instintivo es responder "eso no funcionó, prueba X". Suele ser mejor rebobinar justo después de las lecturas y volver a pedir con lo aprendido: *"No uses el enfoque A, el módulo foo no expone eso — ve directo a B."*

También puedes usar "summarize from here" o `/rewind` para que Claude escriba una nota de handoff antes de rebobinar — como un mensaje del yo futuro que probó algo y descubrió que no servía.

## Compactar vs. limpiar

`/compact` pide al modelo resumir la conversación y reemplaza el historial con ese resumen. Es con pérdida, pero no requiere esfuerzo por tu parte y Claude puede ser minucioso capturando aprendizajes. Puedes guiarlo: `/compact focus on the auth refactor, drop the test debugging`.

`/clear` empieza limpio, pero *tú* escribes qué importa: *"estamos refactorizando el middleware de auth, la restricción es X, los archivos relevantes son A y B, hemos descartado el enfoque Y."* Más trabajo, pero el contexto resultante es exactamente lo que decidiste.

## Por qué a veces falla la auto-compactación

Una mala auto-compactación suele indicar que el modelo no podía predecir tu siguiente dirección. Una sesión larga de depuración se compacta y tu siguiente mensaje es "ahora arregla esa otra advertencia de `bar.ts`". Como la sesión se centraba en depurar, puede que esa advertencia no llegara al resumen.

Esto es especialmente difícil porque el modelo está en su peor momento cuando compacta — el context rot ya está en juego. Con 1M de contexto tienes más tiempo para `/compact` proactivamente con una pista sobre hacia dónde vas.

## Subagentes y contexto fresco

Los subagentes brillan cuando un bloque de trabajo va a producir mucho output intermedio que no necesitarás después.

Cuando Claude lanza un subagente mediante la herramienta Agent, éste recibe una ventana limpia, hace el trabajo, sintetiza el resultado y devuelve solo el informe final. El padre no ve el ruido intermedio.

El test mental de Anthropic: *¿necesitaré esa salida de herramienta otra vez o solo la conclusión?*

Prompts para invocar subagentes explícitamente:

- "Lanza un subagente para verificar el resultado de este trabajo basándose en el siguiente archivo de spec."
- "Lanza un subagente para leer otro codebase y resumir cómo implementaron el flujo de auth, luego impleméntalo tú igual."
- "Lanza un subagente para escribir la documentación de esta funcionalidad basándose en mis cambios de git."

## Tabla resumen

| Situación | Considera | Por qué |
|---|---|---|
| Misma tarea, contexto aún relevante | Continue | Todo en la ventana sigue siendo útil; no pagues por reconstruirlo. |
| Claude fue por mal camino | Rewind (doble Esc) | Conserva las lecturas útiles, descarta el intento fallido, vuelve a pedir con lo aprendido. |
| A mitad de tarea pero la sesión está sobrecargada de depuración/exploración obsoleta | `/compact <hint>` | Poco esfuerzo; Claude decide qué importaba. Guíalo con instrucciones si hace falta. |
| Empiezas una tarea realmente nueva | `/clear` | Cero rot; controlas exactamente qué se lleva. |
| El próximo paso generará mucho output del que solo necesitas la conclusión | Subagente | El ruido intermedio queda en el contexto del hijo; solo vuelve el resultado. |

## Fuente

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — Thariq Shihipar, 15 de abril de 2026.
