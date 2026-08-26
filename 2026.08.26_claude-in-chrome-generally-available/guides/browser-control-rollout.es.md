[English](./browser-control-rollout.en.md) · [한국어](./browser-control-rollout.ko.md) · **Español** · [日本語](./browser-control-rollout.ja.md)

# Desplegar el control del navegador en Chrome

## Qué se lanzó

Claude in Chrome ya está disponible de forma general en todos los planes de pago de Claude, con
acciones autónomas en el navegador respaldadas por verificación de seguridad.

## Para qué sirve

El sentido del control del navegador es el alcance: herramientas sin integración nativa. Paneles
internos para los que nadie construyó un conector, sistemas heredados, portales de proveedores.
Dentro del navegador, Claude puede:

- ver páginas web y actuar sobre ellas: leer texto, hacer clic en enlaces, navegar, rellenar
  formularios;
- trabajar entre pestañas mientras la conversación continúa en las apps de escritorio, móvil y web;
- autenticarse con las sesiones ya iniciadas en el navegador.

Si un sistema ya cuenta con integración nativa, úsala. El control del navegador es la respuesta
para lo que las integraciones no cubren.

## Acciones autónomas

Claude ahora aprueba automáticamente las acciones seguras, con el mismo mecanismo que el modo auto
de Claude Code. Las personas usuarias pueden anular ese comportamiento.

La pregunta de planificación cambia en consecuencia: no "¿se detendrá a preguntar en cada paso?"
sino "¿qué pasos de esta tarea debería ver antes una persona?". Enviar, remitir, comprar, publicar
y cambiar ajustes de cuenta pertenecen a ese conjunto, se apruebe lo que se apruebe
automáticamente.

## Inyección de prompts y las tres defensas

Actores maliciosos ocultan instrucciones en el contenido web —una página, un correo, un campo de
formulario— para redirigir a los agentes de IA. Se han desplegado tres capas de protección:

1. **Entrenamiento reforzado del modelo** frente a una biblioteca creciente de ataques, alimentada
   por automatizadores internos, red-teamers externos y monitorización del mundo real.
2. **Sondas de detección** que analizan el contenido web *antes* de que Claude actúe, avisando al
   modelo de la presencia de un ataque potencial.
3. **Clasificadores de verificación de acciones** que comprueban si la acción se corresponde con lo
   que pidió la persona usuaria.

### Qué mostraron las evaluaciones

Pruebas con ataques reforzados por red-teaming:

| Condición | Tasa de éxito del ataque |
| --- | --- |
| Claude Opus 5, antes de las salvaguardas | 3,8% |
| Con sondas y clasificadores de seguridad — Sonnet 5 | 0% |
| Con sondas y clasificadores de seguridad — Opus 5 | 0% |
| Con sondas y clasificadores de seguridad — Fable 5 | 0,3% |

Son tasas, no garantías. La regla de trabajo sigue siendo la misma: lo que muestra el navegador es
dato, no instrucción.

## Cómo empezar

- **Personas individuales:** instala Claude in Chrome desde la Chrome Web Store.
- **Administradores de empresa:** gestiónalo desde Organization Settings, incluidas las
  restricciones de dominio.

Acotar la lista de dominios es el control principal en el despliegue. Empieza por los sistemas que
el equipo realmente necesita y amplía desde ahí.

## Fuente

- https://claude.com/blog/claude-in-chrome-generally-available (publicado el 2026-08-26)
