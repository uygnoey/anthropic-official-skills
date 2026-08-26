[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Claude tiene su propio navegador en Cowork

## ¿De qué trata este post?

Un anuncio de producto: Claude Cowork en la aplicación de escritorio ya cuenta con un navegador
propio. Cuando una tarea necesita un sitio web, se abre un navegador en el panel lateral y Claude
navega por las páginas, las lee, hace clic y escribe. El post explica en qué se diferencia este
navegador de Claude in Chrome, cuál conviene usar en cada situación, cómo se importan los inicios de
sesión sitio por sitio, qué protege la sesión frente a la inyección de prompts y cómo funciona el
despliegue para los planes de pago y para los administradores empresariales.

## ¿Cuándo es útil?

- Una tarea web debería ejecutarse por su cuenta mientras sigues trabajando en otra ventana.
- Estás decidiendo entre el navegador integrado y Claude in Chrome para un trabajo concreto.
- Quieres que un agente llegue a un sitio sin exponer tus pestañas, marcadores ni contraseñas.
- Eres administrador de una empresa y necesitas activar el navegador integrado para la organización.

## Puntos clave

- **Un navegador dentro de la aplicación de escritorio.** Cuando una tarea necesita un sitio web, se
  abre un navegador en el panel lateral y Claude navega por las páginas, las lee, hace clic y
  escribe.
- **Separado de tu navegación personal.** Claude nunca ve tus pestañas, marcadores ni contraseñas.
- **Los inicios de sesión se importan sitio por sitio**, desde Chrome, Edge o Firefox en macOS, y
  desde Firefox en Windows y Linux. Los sitios de banca, correo y SSO quedan excluidos por defecto,
  salvo que los incluyas explícitamente.
- **Usa el navegador integrado** para trabajo web que debe avanzar mientras sigues siendo productivo
  en otra cosa: reunir investigación, recopilar facturas en portales de proveedores.
- **Usa Claude in Chrome** para páginas que ya tienes abiertas y con sesión iniciada: actualizar un
  CRM, vaciar una bandeja de entrada, editar un documento.
- **El valor por defecto depende de tu historial.** Cambia según si ya usas Claude in Chrome, y
  puedes elegirlo manualmente en Settings → Cowork → Preferred browser.
- **El riesgo es la inyección de prompts.** Instrucciones ocultas en una página intentan desviar a
  Claude. El navegador integrado lleva las mismas salvaguardas que Claude in Chrome, incluida la
  verificación de que las acciones se corresponden con lo que pediste. Estas medidas reducen el
  riesgo de forma significativa, pero no pueden eliminarlo: empieza por sitios de confianza.
- **Despliegue.** A lo largo de la semana para Pro, Max y Team en macOS, Windows y Linux (beta); no
  hace falta configurar nada más allá de encargarle a Claude una tarea web. Los administradores
  empresariales pueden activarlo de inmediato en Organization settings → Cowork → Built-in browser.
- **El navegador vive en el escritorio.** La web y el móvil pueden usarlo mientras la aplicación de
  escritorio esté abierta y conectada; sin ella, quienes solo usan la web siguen con Claude in
  Chrome.

## Recursos incluidos

- `skills/desktop-browser-routing/SKILL.md` — cómo elegir entre el navegador integrado y Claude in
  Chrome, y cómo trabajar con seguridad en cualquiera de los dos.
- `skills/desktop-browser-routing/references/browser-choice.md` — los dos navegadores comparados.
- `skills/desktop-browser-routing/references/logins-and-safety.md` — alcance de la importación de
  inicios de sesión y postura frente a la inyección de prompts.
- `guides/built-in-browser-rollout.{en,ko,es,ja}.md` — despliegue, activación por administrador y
  configuración.

## Fuente

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
