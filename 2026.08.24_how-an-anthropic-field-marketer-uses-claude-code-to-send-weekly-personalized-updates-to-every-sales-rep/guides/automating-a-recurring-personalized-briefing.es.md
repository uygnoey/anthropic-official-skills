[English](./automating-a-recurring-personalized-briefing.en.md) · [한국어](./automating-a-recurring-personalized-briefing.ko.md) · **Español** · [日本語](./automating-a-recurring-personalized-briefing.ja.md)

# Automatizar un briefing periódico personalizado

Una metodología de despliegue para convertir una actualización recurrente hecha a mano en un
sistema automatizado y personalizado por destinatario, tomada de cómo un field marketer de
Anthropic sustituyó una presentación de domingo por la tarde por un resumen del lunes por la
mañana para cada comercial al que daba soporte.

## La forma del problema

La versión manual falla de una manera predecible. Funciona mientras das soporte a un solo equipo.
A medida que asumes más equipos, el tiempo de preparación crece linealmente y lo primero que
recortas es la personalización, que es justo lo que hacía que valiera la pena leer la
actualización. Acabas dedicando más tiempo para entregar algo menos útil.

El objetivo aquí no es la automatización, sino la personalización a escala. La automatización es
lo que hace asequible esa personalización.

## Etapa 1 — Construir rápido la primera versión

El sistema original se construyó en aproximadamente una hora, durante un hackathon de marketing:
un bloque de tiempo reservado para rehacer procesos con Claude.

En esa hora entran tres cosas:

1. **Un briefing que describe el problema de negocio**, contigo situado como product manager del
   resultado y no como el técnico que lo construye. No necesitas saber programar; necesitas
   explicar tu problema con claridad.
2. **Contexto de negocio transmitido como se lo darías a un compañero nuevo.** Grabar una
   explicación en voz del problema funciona bien para la historia y las restricciones que de
   otro modo omitirías.
3. **Un ejemplo de plantilla del resultado deseado**, estructurado como las tres cosas
   principales de la semana, con lo accionable primero.

No intentes acertar con el modelo de datos en esa hora. Consigue un mensaje plausible para un
único destinatario.

## Etapa 2 — Conectar los datos reales

Conecta el almacén de datos en lugar de las herramientas individuales. En el caso original fue
BigQuery a través de MCP, alimentado a su vez por HubSpot, Clay y Salesforce.

El cruce de personalización es: el territorio del comercial en el CRM, las actualizaciones de
cuentas relevantes en Slack, y el emparejamiento con las iniciativas de marketing vigentes. Con
el tiempo, el conjunto de contenidos se amplió a artículos de blog, eBooks, historias de
clientes, webinars y eventos del ecosistema de partners.

Da por hecho que los esquemas de origen se moverán. La hoja de eventos de campo reordenó sus
columnas tres veces en seis semanas. La solución duradera es el mapeo semántico de columnas:
haz que Claude lea la fila de cabeceras y verifique el mapeo antes de procesar, refiriéndose a
"la columna que contiene la URL del evento" y no a una posición fija.

## Etapa 3 — Pilotar con un grupo comprometido

Elige un equipo lo bastante pequeño como para dar feedback real y dispuesto a invertir en darlo.
El piloto original fue un único equipo de ventas de diez comerciales que se comprometieron a
responder.

Envía las primeras ejecuciones a ti mismo antes que a nadie más, y juzga el resultado frente al
estándar de calidad que ya tienes por haber hecho la tarea a mano.

El piloto existe para sacar a la luz fallos que no habrías previsto. En el caso original fueron:

- **Datos inventados.** URLs verosímiles fabricadas para eventos que no tenían enlace de
  inscripción.
- **Fallos de relevancia.** VPs de ingeniería propuestos para talleres de knowledge workers;
  cuentas de retail a las que se mostraban eventos centrados en finanzas.
- **Casos vacíos sin gestionar.** Vendedores nuevos sin cuentas asignadas que recibían mensajes
  en blanco.

## Etapa 4 — Convertir el feedback en reglas explícitas

Esta es la etapa que realmente construye el sistema. Cada corrección se convierte en una regla
documentada dentro del prompt, y se registra qué regla salió de qué feedback. Tras la primera
semana, el prompt original contenía nueve reglas de contenido explícitas.

Entre las reglas que menciona el artículo: nunca inventar una URL y renderizar enlaces solo desde
los datos de origen exactos; verificar los cargos de los contactos frente a la audiencia del
evento; filtrar los eventos por la industria de la cuenta; y escribir una nota de bienvenida a
medida para los vendedores nuevos que aún no tienen cuentas.

Versiona el prompt a medida que crece: cada actualización guardada como una versión numerada con
una nota de cambio de una línea. Empieza en un documento y pasa a una plataforma colaborativa
como GitHub cuando más gente del equipo necesite acceso.

## Etapa 5 — Escalar por duplicación

Cada audiencia adicional es el prompt que ya funciona, copiado, con un campo cambiado: cómo se
asigna esa audiencia a las cuentas en el CRM. Los BDR se asignan de forma distinta a los account
executives, y ahí está toda la diferencia. En el caso original la versión para BDR se lanzó dos
días después de pedirla. Después llegaron customer success, alianzas y socios interfuncionales
fuera de ventas.

## Etapa 6 — Convertirlo en un sistema operativo

- **Archiva cada envío** para auditoría y trazabilidad.
- **Da a los managers un consolidado** de las recomendaciones hechas a su equipo.
- **Pasa de aprobar a revisar.** El punto de llegada es que lees el resultado pero ya no eres una
  barrera para él. El sistema original funcionó solo mientras su autor estaba de vacaciones.

## Qué medir

El artículo reporta un resultado concreto: las inscripciones a una cena ejecutiva se duplicaron en
una semana tras el lanzamiento del resumen, atribuido a que los comerciales adecuados recibían
información relevante el lunes por la mañana. Elige la acción posterior que tu briefing debe
impulsar y mide eso, en lugar de medir el briefing en sí.

## Lista de arranque

1. Elige una tarea repetitiva que ya hagas a mano, para tener un estándar de calidad con el que
   comparar.
2. Informa a Claude en lenguaje llano, como a un compañero nuevo.
3. Envía las primeras ejecuciones a ti mismo.
4. Pilota con un grupo pequeño y comprometido.
5. Convierte cada corrección en una regla y anota qué feedback la produjo.
6. Versiona cada actualización del prompt con una nota de cambio de una línea.
7. Duplica y cambia el campo de asignación para cada nueva audiencia.

## Fuente

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep (publicado el 2026-08-24, por Adam Ward)
