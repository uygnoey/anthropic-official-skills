[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Presentamos routines en Claude Code

## ¿De qué trata este post?

Anuncio de **routines** en Claude Code, en research preview desde el 14 de abril de 2026. Una routine es una automatización de Claude Code que configuras una vez — prompt, repo y conectores — y luego se ejecuta según un horario, mediante una llamada a una API o en respuesta a un evento. Se ejecutan sobre la infraestructura web de Claude Code, así que nada depende de que tu portátil esté abierto.

## ¿Cuándo es útil?

- Ya usas Claude Code para automatizar el ciclo de desarrollo, pero gestionas tú mismo cron jobs, infraestructura y tooling MCP adicional.
- Quieres conectar Claude Code a tus alertas, deploy hooks o herramientas internas mediante endpoints HTTP.
- Quieres que los eventos de PR en GitHub disparen automáticamente una sesión de Claude Code con tu routine.
- Necesitas tareas programadas como triaje nocturno del backlog o escaneo semanal de deriva en la documentación.
- Operas CI/CD y quieres verificación de despliegues, triaje de alertas o flujos feedback→PR dentro de Claude Code.

## Puntos clave

- **Tres tipos de disparador** en research preview: programado (por horas/noches/semanas), API (endpoint HTTP con token de auth por routine) y webhook (empezando por eventos de repos en GitHub).
- Las routines programadas sustituyen al flujo `/schedule` del CLI — las tareas existentes de `/schedule` se convierten en routines.
- Cada routine de API tiene su propio endpoint y token: haces POST de un mensaje y recibes una URL de sesión.
- Las routines por webhook de GitHub abren una sesión de Claude por cada PR que coincida con tus filtros y siguen alimentando esa sesión con las actualizaciones del PR (comentarios, fallos de CI).
- Patrones tempranos comunes: triaje de backlog, deriva documental, verificación de despliegues, triaje de alertas, resolución de feedback, ports de librería entre SDKs, revisión de código a medida.
- Disponibilidad: planes Pro, Max, Team y Enterprise con Claude Code en la web activado. Se crean en claude.ai/code o con `/schedule` en el CLI.
- Límites diarios: Pro hasta 5, Max hasta 15, Team/Enterprise hasta 25 routines al día. Se permite uso extra por encima. Las routines consumen los límites de la suscripción igual que las sesiones interactivas.

## Recursos incluidos

- `skills/code-routines/SKILL.md` — cómo elegir el tipo de disparador y redactar un buen prompt para la routine.
- `skills/code-routines/examples/prompts.md` — los prompts programado, de API y de webhook de GitHub citados en el post.
- `skills/code-routines/references/patterns.md` — lista completa de los patrones de uso temprano del post.
- `guides/routines-overview.{en,ko,es,ja}.md` — guía narrativa en cuatro idiomas.

## Fuente

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — publicado el 14 de abril de 2026.
