[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Claude in Chrome ya está disponible de forma general

## ¿De qué trata este post?

Un anuncio de producto: Claude in Chrome ya está disponible de forma general en todos los planes de
pago de Claude, con acciones autónomas en el navegador respaldadas por verificación de seguridad.
El post explica para qué sirve el control del navegador —alcanzar herramientas sin integración
nativa—, cómo se aprueban ahora automáticamente las acciones seguras, y las tres capas desplegadas
contra la inyección de prompts, con los números de las evaluaciones de red-teaming.

## ¿Cuándo es útil?

- Un flujo de trabajo depende de un panel interno, un sistema heredado o un portal de proveedor que
  ningún conector cubre.
- Estás decidiendo si dejar que un agente actúe dentro de una sesión del navegador y quieres saber
  qué se aprueba automáticamente y qué no.
- Necesitas explicar el riesgo de inyección de prompts y sus mitigaciones a una revisión de
  seguridad.
- Eres administrador de empresa y estás acotando a qué dominios puede llegar el control del
  navegador.

## Puntos clave

- **Disponible de forma general en todos los planes de pago.** Las personas individuales lo
  instalan desde la Chrome Web Store.
- **El caso de uso es el alcance.** Paneles internos, sistemas heredados y portales de proveedores
  sin integración nativa.
- **Qué puede hacer en el navegador.** Ver páginas y actuar sobre ellas —leer texto, hacer clic en
  enlaces, navegar, rellenar formularios—, trabajar entre pestañas y autenticarse con las sesiones
  ya iniciadas, mientras la conversación continúa en las apps de escritorio, móvil y web.
- **Las acciones seguras se aprueban automáticamente**, con el mismo mecanismo que el modo auto de
  Claude Code, y con la posibilidad de que la persona usuaria lo anule.
- **La amenaza son las instrucciones inyectadas.** Actores maliciosos ocultan instrucciones en el
  contenido web —una página, un correo o un campo de formulario— para redirigir a los agentes de IA.
- **Tres capas de protección.** Entrenamiento reforzado del modelo frente a una biblioteca creciente
  de ataques (alimentada por automatizadores internos, red-teamers externos y monitorización del
  mundo real); sondas que analizan el contenido web antes de que Claude actúe; y clasificadores de
  verificación que comprueban que las acciones se corresponden con lo pedido.
- **Resultados de la evaluación.** Frente a ataques reforzados por red-teaming, Claude Opus 5 mostró
  una tasa de éxito del 3,8% antes de las salvaguardas. Con sondas y clasificadores de seguridad:
  0% contra Sonnet 5 y Opus 5, y 0,3% contra Fable 5.
- **Controles de administración.** Los administradores de empresa lo gestionan desde Organization
  Settings, incluidas las restricciones de dominio.

## Recursos incluidos

- `skills/browser-control-safety/SKILL.md` — cuándo encaminar una tarea por el control del navegador
  y cómo trabajar con seguridad una vez que lo haces.
- `skills/browser-control-safety/references/prompt-injection-defenses.md` — el ataque, las tres
  capas y la tabla de evaluación.
- `skills/browser-control-safety/references/rollout-and-admin-controls.md` — disponibilidad,
  capacidades, instalación y administración empresarial.
- `guides/browser-control-rollout.{en,ko,es,ja}.md` — el panorama completo del despliegue en cuatro
  idiomas.

## Fuente

- https://claude.com/blog/claude-in-chrome-generally-available (publicado el 2026-08-26)
