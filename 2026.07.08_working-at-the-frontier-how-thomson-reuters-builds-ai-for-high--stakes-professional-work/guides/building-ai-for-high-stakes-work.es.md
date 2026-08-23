[English](./building-ai-for-high-stakes-work.en.md) · [한국어](./building-ai-for-high-stakes-work.ko.md) · **Español** · [日本語](./building-ai-for-high-stakes-work.ja.md)

# Cómo Thomson Reuters construye IA para trabajo profesional de alto riesgo

Thomson Reuters es una compañía global de contenidos y tecnología con más de 175 años de historia.
Está aplicando IA a flujos de trabajo legales, fiscales, contables, de cumplimiento y profesionales que
exigen precisión.

"Somos una empresa de tecnología centrada en profesiones que exigen exactitud y precisión", explica
Joel Hron, CTO de la compañía. Entre sus productos están Westlaw y Practical Law para investigación
jurídica, y CoCounsel Legal, una plataforma de IA legal de grado profesional diseñada para que los
profesionales del derecho sean más eficaces con respuestas defendibles.

Hron se incorporó a Thomson Reuters hace cuatro años, cuando su startup fue adquirida. Señala que la IA
ha reconfigurado de raíz el desarrollo de software, lo que vuelve críticamente importante la elección
del socio tecnológico.

## La prueba que un modelo debe superar

Thomson Reuters evalúa los modelos de lenguaje preguntando si su trabajo puede resistir una revisión
legal profesional.

La razón de que esa sea la prueba, y no una puntuación de benchmark, está en dónde reside la
responsabilidad:

> "Ese profesional humano sigue siendo quien responde por el producto final del trabajo."

La compañía se apoya en tres ventajas: contenido autorizado, profunda experiencia de dominio e
integración en los flujos de trabajo. El sistema combina los modelos frontera de Anthropic con el
contenido curado de Thomson Reuters, más de 2.700 expertos de dominio e infraestructura de evaluación.

El enfoque tiene nombre: **Fiduciary-Grade AI™**, anclado en contenido autorizado, moldeado por
experiencia de dominio e incrustado en flujos de trabajo profesionales para que los resultados sean
"transparentes, verificables y defendibles cuando hay mucho en juego".

En la práctica, eso implicó reconstruir la investigación jurídica en torno a agentes ajustados para la
validación y verificación de citas, y no solo para buscar y recuperar, de modo que los profesionales
puedan revisar, verificar y aplicar su criterio con confianza.

## Construir un producto centrado en agentes

En lugar de crear chatbots más listos, Thomson Reuters reconstruyó sus productos como sistemas basados
en agentes. Un único agente accede ahora a cientos de herramientas de la compañía simultáneamente.

> "Nuestra gran prueba para Claude es evaluar lo bueno que es haciendo planes y usando herramientas de
> forma eficaz."

CoCounsel Legal es el ejemplo. Antes ejecutaba habilidades separadas de forma secuencial; ahora está
reconstruido sobre el Claude Agent SDK, planificando y orquestando entre herramientas en tiempo real.
Los datos de los clientes siguen protegidos y no se usan para entrenar modelos de terceros.

Thomson Reuters eligió a Anthropic por sus enfoques de transparencia, seguridad y desarrollo
responsable de la IA. La primera prueba llegó con capacidades de investigación profunda construidas de
forma conjunta.

## Qué exige el trabajo del conocimiento a un modelo

Cuatro requisitos debían cumplirse antes de confiar este trabajo a un modelo:

1. **Validación de citas.** El sistema debe comprobar las citas antes de presentar los hallazgos para
   revisión humana.
2. **Gestión del contexto.** Los modelos deben mantener la continuidad del hilo a lo largo de cadenas
   extensas de uso de herramientas.
3. **Colaboración humana.** Los modelos deben "incorporar a la persona al desarrollo del producto de
   trabajo, en lugar de limitarse a depender del agente".
4. **Ampliación de capacidades.** Redacción avanzada para trabajo complejo, incluidas mociones y
   escritos que los profesionales "pasarían días o semanas perfeccionando".

## La cuestión del retorno

La posición de Hron aquí es deliberadamente a contracorriente:

> "Si intentas optimizar demasiado el cálculo de la tasa de retorno, los árboles no te dejan ver el
> bosque."

Antepone los cambios culturales de mentalidad a la optimización de métricas de coste por tarea. La
compañía sigue midiendo indicadores de ingeniería como DORA y el tiempo hasta producción, y tiene
resultados concretos que señalar: una herramienta interna de remediación de errores construida sobre
Claude redujo el análisis de causa raíz de tres horas a cuatro minutos.

Pero el cambio de fondo afecta al trabajo mismo. Sobre los ingenieros, Hron observa: "El acto de
escribir líneas de código ya no es el trabajo." Ahora lo que más pesa son el pensamiento sistémico, el
criterio y el buen gusto. El mismo patrón se extiende por las organizaciones y hace a las personas "más
en forma de T", capaces de alcanzar producto, diseño y finanzas.

## Qué viene después

El equipo de Hron prioriza el trabajo de horizonte más largo, una mejor gestión del contexto y llamadas
a herramientas fiables a lo largo de las cadenas de tareas del agente. Él mismo usa Claude Code para
familiarizarse rápidamente con bases de código y Claude Cowork para análisis estratégico.

Para un trabajo que "en última instancia tiene que sostenerse ante un tribunal", ve el empuje de las
capacidades del modelo como "la frontera que merece la pena empujar a continuación. Al fin y al cabo,
la IA profesional tiene que funcionar en entornos donde estar casi en lo cierto no es suficiente."

## Fuente

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Blog de Claude, 8 de julio de 2026.
