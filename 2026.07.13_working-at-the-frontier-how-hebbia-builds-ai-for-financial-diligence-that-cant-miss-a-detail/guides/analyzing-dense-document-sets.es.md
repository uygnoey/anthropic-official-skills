[English](./analyzing-dense-document-sets.en.md) · [한국어](./analyzing-dense-document-sets.ko.md) · **Español** · [日本語](./analyzing-dense-document-sets.ja.md)

# Cómo Hebbia analiza conjuntos densos de documentos sin que se le escape un detalle

Hebbia es una plataforma de IA que da servicio a más de un tercio de las 50 principales gestoras de
activos, además de a bancos de inversión y despachos de abogados de primer nivel. Sus clientes toman
decisiones a partir de análisis que abarcan miles de documentos densos, donde la exactitud es crítica.

Divya Mehta, la primera product manager de la compañía, trabaja estrechamente con grandes clientes de
banca de inversión, capital privado y crédito. Adithya Ramanathan dirige el equipo de investigación de
IA aplicada, centrado en encontrar señales logrando que los modelos se apoyen en los datos correctos,
en el contexto correcto, y saquen a la luz lo que los clientes necesitan saber.

## El problema

Los banqueros e inversores que evalúan una oportunidad deben recorrer todos los datos relevantes:
documentos regulatorios públicos, contratos de crédito, documentos internos y datos estructurados
procedentes de los CRM. La información que otorga ventaja competitiva suele residir en documentos
propietarios y no estructurados, históricamente más difíciles de analizar a escala que los datos
cuantitativos y estructurados que las finanzas ya modelan con soltura.

Hebbia construyó Matrix para sistematizar ese trabajo cualitativo, y cada generación de modelos ha
ampliado lo que puede hacer.

## Cómo funciona Matrix

El meta-prompting de Hebbia convierte peticiones en lenguaje natural en prompts, y Claude analiza cada
paso a lo largo de cientos de documentos. Las respuestas aparecen en celdas individuales de una
cuadrícula dentro de Matrix, y es precisamente esa disposición la que da al análisis transparencia,
trazabilidad y capacidad de dirección plenas.

Así formula Ramanathan el objetivo:

> "Cuando lo conectas a los datos correctos y lo pones en el ecosistema correcto, ahí es cuando
> obtienes el alfa que los profesionales de las finanzas persiguen de verdad."

## Cómo se evalúan los modelos nuevos

El equipo pasa cada modelo nuevo por el benchmark específico de finanzas de Hebbia, comparándolo cara a
cara con el modelo al que sustituiría, y amplía las mediciones del benchmark con cada lanzamiento.

Mehta, sobre el listón: "El listón es extremadamente alto, y nuestros clientes nos obligan a mantenerlo
ahí, y con razón."

Joe Renner, investigador del equipo de IA aplicada, prueba cada nuevo modelo de Claude contra el
benchmark, replicando casos de uso clave del trabajo de conocimiento en finanzas. Hay dos pruebas:

1. **Respuesta a preguntas y localización de citas** sobre documentos financieros.
2. **Una ejecución a través del sistema de agentes de Hebbia** con las herramientas del producto de
   chat, simulando análisis abierto y multifuente.

Claude Fable 5 superó ambas pruebas con el margen más amplio que Renner había medido.

En la prueba de respuesta y citas, logró una mejora de exactitud relativa de aproximadamente el 20%
sobre documentos financieros: el mejor resultado que Renner había registrado de un modelo nuevo. La
coincidencia de citas se mantuvo más o menos estable; Renner atribuye la mejora a que el modelo entiende
mejor la evidencia que identifica.

Mehta reduce el trabajo a dos cualidades:

> "Se reduce a dos cualidades aparentemente fundamentales: la capacidad de encontrar la información
> correcta en un conjunto de datos denso, y luego sintetizarla correctamente."

En la ejecución con agentes, el modelo sostuvo simultáneamente todos los componentes de peticiones de
varias partes, respondió a todos y citó cada respuesta a su fuente.

También mostró mayor alcance. En el análisis abierto razonó a partir de una sección transversal más
amplia de los datos y llegó a conclusiones que el equipo consideró dignas de un examen más detenido.
Renner lo atribuye a cómo el modelo mantiene la coherencia en tareas largas: conservar cada parte de la
petición a la vista, dar instrucciones a sus propios subagentes y herramientas para recuperar los hechos
pertinentes, y anclar cada afirmación en su fuente en lugar de inferirla.

## Qué hace posible

**Salas de datos.** Miles de documentos donde el trabajo consiste en encontrar señales relevantes,
citarlas y redactar secciones de un memorando de inversión.

**Operaciones de crédito.** Todos los documentos ligados a una operación —contratos de crédito,
modificaciones, side letters de cientos de páginas técnicas y densas— de cuya masa no estructurada se
extraen el paquete completo de covenants, los términos financieros y las restricciones operativas.

Mehta, sobre este tipo de material: "En realidad, estos son precisamente los documentos con los que los
modelos de Anthropic siempre se han desenvuelto muy bien."

Con los modelos Sonnet y Opus anteriores, Matrix ya podía extraer y sintetizar los covenants de los
contratos de crédito, esas protecciones densas que los prestamistas redactan para sí mismos. Con Claude
Fable 5, Hebbia persigue el trabajo completo: análisis en varios pasos sobre esos covenants, comparación
con datos de monitorización en vivo, señalización de riesgos y primeros borradores de revisiones de
covenants y memorandos internos. Ese trabajo de revisión exigía tradicionalmente que las firmas de
crédito pagaran sumas considerables a equipos externos por un análisis hecho a mano.

## La medida que sustituyó a la anterior

Con modelos capaces de llevar el trabajo de principio a fin, la comparación se centra en las horas de
especialista sustituidas.

Históricamente, cuando un managing director necesitaba una presentación para un CEO, un banquero junior
dedicaba de dos a tres días a estudiar la empresa, reunir los datos financieros y montar las
diapositivas. En la época anterior a Opus, ese plazo se comprimió entre 12 y 24 horas. Con los modelos
Opus anteriores sobre Hebbia, Mehta indica que bajó a aproximadamente un día de principio a fin. Después
Hebbia codificó el trabajo entero en un Matrix que reúne datos de varias fuentes mediante pasos
agénticos deterministas, realiza el análisis y construye las presentaciones finales, los modelos
financieros y la investigación interna, en un par de minutos. Los banqueros dedican ese tiempo a
identificar compradores y a definir el posicionamiento. Claude Fable 5 aprieta todavía más ese plazo.

## Por qué la descomposición sobrevive a los modelos capaces

Descomponer el trabajo en pasos sigue siendo importante "por brillante que sea el modelo", porque las
firmas exigen control sobre qué documentos alimentan el análisis y cómo se construye cada paso. Hebbia
está adoptando el Claude Agent SDK para componer estos trabajos como pasos más pequeños, repetibles y
verificados, en lugar de ejecuciones únicas del modelo.

## Qué piden ahora los clientes

> "Hace dos o tres años las preguntas eran defensivas: sobre alucinaciones y sobre si las cuentas
> cuadraban. Hoy esas conversaciones han cambiado por completo. Son: ¿cómo automatizo más partes de mi
> flujo de trabajo? ¿Cómo encadeno más pasos? ¿Cómo genero diez, quince, veinte presentaciones de un
> solo clic, con alta fidelidad y consistencia?" — Divya Mehta

## Fuente

[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Blog de Claude, 13 de julio de 2026.
