[English](./routines-overview.en.md) · [한국어](./routines-overview.ko.md) · **Español** · [日本語](./routines-overview.ja.md)

# Routines en Claude Code: visión general

Recorrido narrativo por *Introducing routines in Claude Code* (14 de abril de 2026, research preview).

## Qué son las routines

Una routine es una automatización de Claude Code que configuras una vez — prompt, repo y conectores — y que después se ejecuta según un horario, mediante una llamada a una API o en respuesta a un evento. Las routines corren sobre la infraestructura web de Claude Code, así que no dependen de tener el portátil abierto.

Los desarrolladores ya automatizan el ciclo de desarrollo con Claude Code, pero hasta ahora gestionaban cron jobs, infraestructura y tooling MCP adicional por su cuenta. Las routines vienen con tus repos y conectores ya conectados, así que empaquetas la automatización una sola vez.

## Los tres tipos de disparador

### Routines programadas

Dale a Claude Code un prompt y una cadencia — horaria, nocturna o semanal — y se ejecuta con ese horario. Ejemplo del anuncio:

> Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.

Si estabas usando `/schedule` en el CLI, esas tareas ahora son routines programadas.

### Routines de API

Cada routine recibe su propio endpoint y token de auth. POST a ese endpoint, recibes una URL de sesión. Puedes enchufar Claude Code a tu sistema de alertas, a tus deploy hooks, a tus herramientas internas — a cualquier cosa que pueda hacer una petición HTTP. Ejemplo de prompt:

> Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.

### Routines por webhook (empezando por GitHub)

Suscribe una routine para que se dispare en respuesta a eventos de repositorios de GitHub. Claude crea una sesión nueva por cada PR que cumpla tus filtros y ejecuta la routine. Ejemplo:

> Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.

Claude abre una sesión por PR y sigue alimentando esa sesión con las actualizaciones del PR (comentarios, fallos de CI), de modo que puede responder a follow-ups. El post indica que se prevé ampliar los webhooks a más fuentes de eventos en el futuro.

## Qué están construyendo los equipos

### Programadas
- **Gestión de backlog**: triar nuevas issues cada noche, etiquetar, asignar y publicar un resumen en Slack.
- **Deriva documental**: escanear semanalmente los PRs mergeados, señalar docs que referencien APIs modificadas y abrir PRs de actualización.

### API
- **Verificación de despliegue**: tu pipeline de CD postea tras cada deploy; Claude ejecuta smoke checks contra el nuevo build, escanea logs de error para detectar regresiones y publica un go/no-go en el canal de release.
- **Triaje de alertas**: apunta Datadog al endpoint de la routine; Claude extrae el trace, lo correlaciona con despliegues recientes y deja un fix borrador listo antes de que el on-call abra la página.
- **Resolución de feedback**: un widget de feedback de docs o un dashboard interno envía el reporte; Claude abre una sesión contra el repo con el issue en contexto y redacta el cambio.

### GitHub
- **Port de librería**: cada PR mergeado a un SDK Python dispara una routine que porta el cambio al SDK Go paralelo y abre un PR equivalente.
- **Revisión de código a medida**: al abrirse un PR, ejecuta la checklist propia del equipo en seguridad y rendimiento, dejando comentarios inline antes de que mire un revisor humano.

## Cómo empezar

Las routines están disponibles para usuarios de Claude Code en planes Pro, Max, Team y Enterprise con Claude Code en la web activado. Ve a claude.ai/code para crear tu primera routine, o escribe `/schedule` en el CLI.

Las routines consumen los límites de uso de la suscripción igual que las sesiones interactivas. Topes diarios:

- Pro: hasta 5 routines al día
- Max: hasta 15 routines al día
- Team y Enterprise: hasta 25 routines al día

Puedes ejecutar más allá de esos topes con uso extra. Consulta la documentación para más información.

## Fuente

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — 14 de abril de 2026.
