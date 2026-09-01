[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo usan Claude Tag los empleados de Anthropic

## ¿De qué trata este post?

Tres relatos de equipos de Anthropic trabajando con Claude Tag — Claude dentro de herramientas de
chat como Slack. Una persona de marketing de producto convierte un hilo largo en un one-pager listo
para revisión; alguien de estrategia de producto consolida peticiones de funcionalidad repartidas
por varios canales; un abogado de producto opera un canal de revisión que filtra los activos de
marketing antes de que los vea el equipo legal. Cada relato incluye la forma del prompt, el tiempo
empleado y lo que la persona se reservó para sí.

## ¿Cuándo es útil?

- Una decisión o una especificación está enterrada en un hilo y alguien la necesita como documento.
- La misma petición reaparece en distintos canales y nadie tiene la lista consolidada.
- Una cola de revisión especializada es el cuello de botella y la mayoría de sus elementos están
  bien.
- Estás decidiendo qué puede hacer un agente dentro del chat y con qué acceso.

## Puntos clave

- **Etiquétalo en un hilo y trabaja con el contexto de la conversación.** Sigue el hilo, aplica
  instrucciones permanentes y decide cuándo intervenir.
- **De hilo a documento: 45 minutos.** Un hilo de más de 15 mensajes se convirtió en un one-pager
  listo para revisión. Claude redactó dos páginas en dos minutos — descripción de la funcionalidad,
  justificación de negocio, detalles de implementación y anexo — y siguieron cuatro rondas de
  verificación.
- **La verificación es tarea humana.** Claude separó lo que había verificado de lo que requería la
  aprobación del responsable de producto; la persona aportó recursos oficiales y Claude reescribió.
- **Consolidación: unos 26 minutos.** Cerca de 20 variantes de búsqueda entre canales, deduplicadas,
  con unas 24 cuentas y el identificador de quien lo pidió, su equipo, el nombre de la cuenta y el
  enlace de origen.
- **La versión semanal: 50 minutos.** Unos 120 informes en bruto se convirtieron en 23 incidencias
  abiertas y 14 resueltas por área de producto — un trabajo estimado en una semana a mano.
- **Estructura del prompt de consolidación:** objetivos de búsqueda, qué cuenta como coincidencia y
  el formato de salida con un ejemplo.
- **Canal de revisión: de un día a 30 minutos por activo.** Claude detecta afirmaciones sin
  respaldo, verifica declaraciones factuales, señala problemas con correcciones concretas y trabaja
  directamente con quien lo solicita. En una newsletter señaló tres puntos y resolvió uno por su
  cuenta.
- **Instrucciones que mejoran solas.** Una corrección se convirtió en instrucción permanente, y una
  rutina de los viernes hace que Claude proponga actualizaciones a partir del feedback de la semana,
  para su aprobación.
- **El acceso está deliberadamente acotado** a los canales y documentos concedidos, y se avisa al
  usuario cuando falta el acceso que la tarea necesita.
- **Disponibilidad:** planes Team y Enterprise a través del servicio propio de Anthropic, con
  configuración en claude.ai/admin-settings/claude-tag. Actualmente en beta pública.

## Recursos incluidos

- `skills/slack-thread-delegation/SKILL.md` — qué delegar en el chat, cómo formular el prompt según
  la forma del trabajo y cómo mantener el resultado fiable.
- `skills/slack-thread-delegation/references/prompt-patterns.md` — las estructuras de prompt de
  síntesis, consolidación y revisión al completo.
- `skills/slack-thread-delegation/examples/tag-workflows.md` — los tres casos con prompts, tiempos y
  resultados.
- `skills/slack-thread-delegation/templates/review-channel-instructions.md` — instrucciones
  permanentes rellenables para un canal de revisión.
- `guides/chat-tag-deployment.{en,ko,es,ja}.md` — patrones de despliegue, acceso y gobernanza, y una
  secuencia de implantación.

## Fuente

<https://claude.com/blog/how-anthropic-employees-use-claude-tag> (2026-08-28)
