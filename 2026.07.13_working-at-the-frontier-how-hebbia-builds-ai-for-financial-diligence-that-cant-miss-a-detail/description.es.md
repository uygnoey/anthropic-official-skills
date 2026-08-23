[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Hebbia es una plataforma de IA que usan más de un tercio de las 50 principales gestoras de activos, junto con bancos de inversión y despachos de abogados de primer nivel. Sus clientes deciden a partir de análisis que abarcan miles de documentos densos, donde la exactitud es crítica. Este post recoge el relato de tres personas que construyen ese sistema —la primera product manager, Divya Mehta; el responsable de investigación de IA aplicada, Adithya Ramanathan; y el investigador Joe Renner— sobre cómo mantienen el listón de la exactitud y cómo decidieron que Claude Fable 5 estaba listo.

Lo recorren dos hilos. El primero es Matrix, el producto de Hebbia para sistematizar el trabajo cualitativo: el meta-prompting convierte una petición en lenguaje natural en prompts, el modelo analiza cada paso a lo largo de cientos de documentos y las respuestas aterrizan en celdas individuales de una cuadrícula, que es lo que hace todo el proceso transparente, trazable y dirigible. El segundo es el benchmark específico de finanzas por el que pasa cada modelo nuevo, siempre cara a cara con el modelo al que sustituiría.

## ¿Cuándo es útil?
- Cuando el análisis debe recorrer miles de documentos densos y no estructurados, y que se escape un detalle cuesta dinero.
- Cuando hay que decidir si adoptar un modelo nuevo y las puntuaciones públicas no son la evidencia que se necesita.
- Cuando se construye un benchmark interno para un dominio donde el listón de exactitud lo fijan los clientes.
- Cuando una cifra del benchmark da un salto y hay que saber qué mitad del trabajo mejoró realmente.
- Cuando se elige entre una única ejecución larga del modelo y una cadena descompuesta paso a paso.
- Cuando se quiere convertir un flujo de trabajo experto de varios días en algo repetible.

## Puntos clave
- **El alfa está en la conexión, no solo en el modelo.** "Cuando lo conectas a los datos correctos y lo pones en el ecosistema correcto, ahí es cuando obtienes el alfa que los profesionales de las finanzas persiguen de verdad." — Adithya Ramanathan
- **Celdas, no una respuesta larga.** Las respuestas aparecen en celdas individuales de una cuadrícula en Matrix, y eso es lo que da al análisis transparencia, trazabilidad y capacidad de dirección plenas.
- **El meta-prompting hace la descomposición.** Las peticiones en lenguaje natural se convierten en prompts; Claude analiza cada paso a lo largo de cientos de documentos.
- **Dos cualidades son todo el trabajo.** "La capacidad de encontrar la información correcta en un conjunto de datos denso, y luego sintetizarla correctamente." — Divya Mehta
- **Cada modelo se compara cara a cara con el que sustituiría,** en un benchmark específico de finanzas cuyas mediciones se amplían con cada lanzamiento.
- **Dos formas de prueba.** Respuesta a preguntas y localización de citas sobre documentos financieros; y una ejecución a través del sistema de agentes con las herramientas del producto de chat, simulando análisis abierto y multifuente.
- **Fable 5 superó ambas con el margen más amplio que Renner había medido:** alrededor de un 20% de mejora relativa de exactitud en la prueba de respuesta, el mejor resultado que había registrado de un modelo nuevo.
- **Las citas se mantuvieron mientras la exactitud subía.** Renner atribuye la mejora a que el modelo entiende mejor la evidencia que identifica, no a que encuentre evidencia distinta.
- **Las peticiones de varias partes se sostuvieron enteras.** Todos los componentes a la vez, todos respondidos, cada respuesta citada a su fuente.
- **La coherencia en tareas largas explica el mayor alcance:** conservar cada parte de la petición a la vista, dar instrucciones a sus propios subagentes y herramientas para obtener hechos, y anclar cada afirmación en su fuente en lugar de inferirla.
- **En crédito, ahora se persigue el trabajo completo.** Los modelos anteriores ya extraían y sintetizaban covenants; con Fable 5 Hebbia va a por el análisis en varios pasos sobre ellos, la comparación con datos de monitorización en vivo, la señalización de riesgos y los primeros borradores de revisiones y memorandos: trabajo por el que las firmas de crédito pagaban tradicionalmente sumas considerables a equipos externos.
- **La cronología de la presentación:** 2–3 días de un banquero junior históricamente → 12–24 horas menos antes de Opus → alrededor de un día con los modelos Opus anteriores → un par de minutos una vez codificado como Matrix. Fable 5 lo aprieta más.
- **La descomposición sobrevive a los modelos mejores.** Sigue siendo importante "por brillante que sea el modelo", porque las firmas exigen control sobre qué documentos alimentan el análisis y cómo se construye cada paso. Hebbia está adoptando el Claude Agent SDK para componer los trabajos como pasos más pequeños, repetibles y verificados.
- **Las preguntas de los clientes se han invertido:** de las alucinaciones y de si las cuentas cuadraban, a cuánto más del flujo de trabajo se puede automatizar y encadenar.

## Recursos incluidos
- `skills/document-grounded-analysis/SKILL.md` — descomponer la petición, dar a cada respuesta su celda con una cita, sostener todas las partes de una petición múltiple y anclar las afirmaciones en lugar de inferirlas.
- `skills/document-grounded-analysis/references/decomposition.md` — por qué la descomposición sobrevive a los modelos capaces, de qué se componen los pasos y qué deja sin especificar el post.
- `skills/document-grounded-analysis/templates/analysis-grid.md` — el diseño de la cuadrícula, un registro de pasos y una comprobación de recuperación frente a síntesis.
- `skills/document-grounded-analysis/examples/diligence-workflows.md` — el análisis de salas de datos, la revisión de covenants de crédito y el trabajo codificado de la presentación.
- `skills/domain-model-benchmarking/SKILL.md` — construir el benchmark desde tu dominio, ejecutar dos formas de prueba, comparar cara a cara y leer exactitud y citas como señales separadas.
- `skills/domain-model-benchmarking/references/benchmark-shape.md` — todo lo que el post afirma sobre el benchmark y las preguntas que no responde.
- `skills/domain-model-benchmarking/templates/model-eval-record.md` — un registro cara a cara con veredictos separados de recuperación y síntesis.
- `skills/domain-model-benchmarking/examples/fable-5-evaluation.md` — la evaluación de Fable 5, sus cifras y qué hizo el equipo con el resultado.
- `guides/analyzing-dense-document-sets.{en,ko,es,ja}.md` — el relato completo en cuatro idiomas.

## Fuente
[Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail](https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail) — Blog de Claude, 13 de julio de 2026.
