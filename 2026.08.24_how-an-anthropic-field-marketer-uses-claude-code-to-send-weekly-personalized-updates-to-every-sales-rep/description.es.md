[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo un field marketer de Anthropic usa Claude Code para enviar actualizaciones semanales personalizadas a cada comercial

## ¿De qué trata este post?

Adam Ward, field marketer en Anthropic, cuenta cómo sustituyó una presentación que preparaba a mano los domingos por la tarde por un sistema automatizado que genera un resumen personalizado el lunes por la mañana para cada comercial al que da soporte. La primera versión se construyó en aproximadamente una hora durante un hackathon de marketing y se fue endureciendo con varias semanas de feedback del piloto.

La tesis central de Ward es que los responsables de marketing no necesitan saber programar: necesitan explicar con claridad su problema de negocio. Empezó con un prompt que lo situaba como product manager y no como técnico, grabó explicaciones en voz para dar contexto de negocio a Claude y aportó ejemplos de plantilla que mostraban el formato de salida deseado.

## ¿Cuándo es útil?

- Envías una actualización recurrente (semanal o mensual) cuya personalización manual consume mucho tiempo.
- Das soporte a varios equipos y hay que recortar el mismo briefing para cada audiencia.
- Tienes datos de CRM, eventos y contenido repartidos en varios sistemas y necesitas emparejarlos con responsables concretos.
- Quieres una ruta de despliegue que empiece como un bucle de autorrevisión y solo después pase a envío autónomo.

## Puntos clave

- **Empieza por el problema de negocio.** Informa a Claude como informarías a un compañero recién incorporado. Ward se presentó como product manager, no como técnico, y grabó explicaciones en voz del problema para transmitir contexto de negocio.
- **Muestra el formato que quieres.** Los ejemplos de plantilla del resultado deseado —estructurados como las "tres cosas principales de la semana", priorizando lo accionable— funcionaron mejor que las instrucciones abstractas.
- **Conecta los datos reales.** Claude se conectó a BigQuery mediante MCP, la fuente de datos de marketing que a su vez extrae de HubSpot, Clay y Salesforce. La personalización sale del territorio del comercial en el CRM, de las actualizaciones de cuentas relevantes en Slack y del cruce con las iniciativas de marketing.
- **Convierte cada corrección en una regla explícita.** Tras la primera semana el prompt contenía nueve reglas de contenido explícitas, cada una rastreable a un feedback concreto: nunca inventar una URL y renderizar solo enlaces presentes en los datos de origen exactos; verificar el cargo del contacto frente a la audiencia del evento; poner una barrera por industria para que las cuentas de retail no reciban eventos centrados en finanzas; y escribir una nota de bienvenida a medida para vendedores nuevos que aún no tienen cuentas asignadas.
- **Haz que el prompt sobreviva a los cambios de esquema.** La hoja de eventos de campo reordenó sus columnas tres veces en seis semanas. La solución fue pedir a Claude que leyera primero la fila de cabeceras y verificara el mapeo de columnas, con instrucciones semánticas como "mira la columna que contiene la URL del evento" en lugar de referencias fijas a columnas.
- **Pilota con un grupo comprometido.** Un equipo de ventas de diez comerciales que aceptó dar feedback sacó a la luz los fallos de calidad de datos y de relevancia antes de un despliegue más amplio.
- **Escalar es copiar y cambiar un campo.** Cuando los BDR pidieron su propia versión, Ward duplicó el prompt y cambió el único campo que describe cómo se asignan los BDR a las cuentas en el CRM; se lanzó en dos días. Después llegaron versiones para customer success, alianzas y socios interfuncionales fuera de ventas.
- **Impacto medible.** Las inscripciones a una cena ejecutiva se duplicaron en una semana tras el lanzamiento del resumen. Cada envío del lunes se archiva para auditoría, los managers reciben consolidados de su equipo y el sistema funcionó solo mientras Ward estaba de vacaciones.

## Recursos incluidos

- `skills/personalized-weekly-digests/SKILL.md` — construir y operar un resumen personalizado recurrente con Claude Code.
- `skills/personalized-weekly-digests/templates/kickoff-prompt.md` — el briefing inicial que plantea el problema de negocio.
- `skills/personalized-weekly-digests/templates/digest-message-template.md` — la forma del mensaje de "tres cosas principales".
- `skills/personalized-weekly-digests/references/content-rules.md` — el catálogo de reglas derivado del feedback del piloto.
- `skills/personalized-weekly-digests/references/data-sources.md` — conexión de datos y gestión de cambios de esquema.
- `skills/personalized-weekly-digests/examples/feedback-to-rule.md` — conversiones de feedback a regla resueltas.
- `guides/automating-a-recurring-personalized-briefing.{en,ko,es,ja}.md` — la metodología de despliegue en cuatro idiomas.

## Fuente

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep (publicado el 2026-08-24, por Adam Ward)
