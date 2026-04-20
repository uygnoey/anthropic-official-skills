[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Claude Code: gestión de sesiones y contexto de 1M

## ¿De qué trata este post?

Una guía práctica del equipo de Claude Code sobre cómo gestionar sesiones y la ventana de contexto — ahora hasta un millón de tokens — para obtener mejores resultados. Presenta el nuevo comando `/usage`, explica el *context rot* y la compactación, y plantea cada turno como un punto de ramificación entre cinco opciones: continuar, `/rewind`, `/clear`, `/compact` o delegar a un subagente.

## ¿Cuándo es útil?

- Ejecutas sesiones largas de Claude Code y notas que la calidad empeora con el tiempo.
- No tienes claro si conviene `/compact`, `/clear`, rebobinar o lanzar un subagente.
- Necesitas un modelo mental para decidir cuándo el contexto sigue siendo útil y cuándo hay que descartarlo.
- Has tenido malas auto-compactaciones y quieres entender por qué.
- Buscas prompts concretos para delegar trabajo a subagentes.

## Puntos clave

- La ventana de contexto incluye el system prompt, toda la conversación, cada llamada de herramienta y su salida, y cada archivo leído. Es un corte duro.
- **Context rot**: el rendimiento del modelo cae al crecer el contexto porque la atención se dispersa y el contenido antiguo distrae de la tarea actual.
- **Compactación**: cuando la ventana se llena, el historial se reemplaza por un resumen escrito por el modelo. También puedes dispararla con `/compact <hint>`.
- Cada turno es un punto de ramificación: Continue, `/rewind` (doble Esc), `/clear`, `/compact` o subagente.
- Regla práctica: **nueva tarea ⇒ nueva sesión**. Pero un seguimiento relacionado (p. ej. documentar lo que acabas de construir) se beneficia de mantener el contexto.
- **Rebobinar en vez de corregir**: cuando Claude va por mal camino, usa `/rewind` justo después de las lecturas útiles y vuelve a pedir con lo aprendido, en lugar de decir "eso no funcionó".
- **Compact vs Clear**: compact pierde información pero requiere poco esfuerzo; clear exige más trabajo pero controlas qué sobrevive.
- **Malas auto-compactaciones** ocurren cuando el modelo no puede predecir tu siguiente dirección — compacta proactivamente con un hint antes de llenar la ventana.
- **Subagentes**: ideales cuando el siguiente paso producirá mucho output intermedio que no necesitas conservar. Test mental: *¿necesitaré esa salida de herramienta otra vez o solo la conclusión?*

## Recursos incluidos

- `skills/context-window-management/SKILL.md` — marco de decisión continue / rewind / compact / clear / subagent.
- `skills/context-window-management/references/decision-table.md` — tabla situación → herramienta del post.
- `skills/context-window-management/examples/subagent-prompts.md` — prompts de delegación a subagentes citados en el post.
- `guides/session-management-1m-context.{en,ko,es,ja}.md` — guía narrativa en cuatro idiomas.

## Fuente

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — publicado el 15 de abril de 2026.
