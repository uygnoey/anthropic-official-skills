[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Thomson Reuters es una compañía de contenidos y tecnología con 175 años de historia que aplica IA a flujos de trabajo legales, fiscales, contables, de cumplimiento y otros que exigen precisión. Este post recoge el relato de su CTO, Joel Hron, sobre cómo la compañía decide si un modelo está a la altura de un trabajo que debe sostenerse ante un tribunal, y qué cambió en sus productos cuando decidió que uno lo estaba.

La idea que lo organiza todo es dónde reside la responsabilidad. "Ese profesional humano sigue siendo quien responde por el producto final del trabajo", y por eso la prueba que se aplica a un modelo es si su trabajo resiste una revisión legal profesional, no una puntuación de benchmark. El nombre que la compañía da al enfoque resultante es Fiduciary-Grade AI™: anclado en contenido autorizado, moldeado por experiencia de dominio, incrustado en flujos de trabajo profesionales.

La segunda mitad es arquitectónica. En lugar de construir chatbots más listos, Thomson Reuters reconstruyó sus productos como sistemas basados en agentes: CoCounsel Legal pasó de ejecutar habilidades separadas de forma secuencial a un único agente sobre el Claude Agent SDK, que planifica y orquesta entre cientos de herramientas en tiempo real.

## ¿Cuándo es útil?
- Cuando el resultado debe sobrevivir a la revisión de alguien que responde por él y "casi correcto" es un fracaso.
- Cuando hay que decidir qué exigirle a un modelo antes de confiarle trabajo regulado o de alto riesgo.
- Cuando un producto es un conjunto de funciones sueltas y son los usuarios quienes las encadenan.
- Cuando se evalúa un modelo para un agente que planifica sobre una gran superficie de herramientas.
- Cuando se diseña en qué momento, respecto de la revisión humana, se comprueban las citas.
- Cuando hay que informar sobre una iniciativa de IA y lo único que se pide es el coste por tarea.

## Puntos clave
- **La prueba es la revisión profesional, no un benchmark.** Thomson Reuters evalúa los modelos preguntando si su trabajo resiste una revisión legal profesional.
- **La IA no altera la responsabilidad.** "Ese profesional humano sigue siendo quien responde por el producto final del trabajo." — Joel Hron
- **Tres ventajas, un sistema.** Contenido autorizado, profunda experiencia de dominio e integración en los flujos de trabajo: los modelos frontera de Anthropic combinados con contenido curado, más de 2.700 expertos de dominio e infraestructura de evaluación.
- **Fiduciary-Grade AI™** significa que los resultados son "transparentes, verificables y defendibles cuando hay mucho en juego".
- **La investigación jurídica se reconstruyó en torno a la verificación.** Agentes ajustados para validar y verificar citas, y no solo para buscar y recuperar, de modo que los profesionales revisen, verifiquen y apliquen su criterio con confianza.
- **Cuatro requisitos antes de confiar en un modelo:** validación de citas antes de la revisión humana; gestión del contexto a lo largo de cadenas extensas de uso de herramientas; colaboración humana —incorporar a la persona al desarrollo del producto de trabajo en lugar de depender del agente—; y ampliación de capacidades hacia la redacción avanzada, incluidas mociones y escritos que llevarían días o semanas perfeccionar.
- **Agentes primero, no chatbots más listos.** Un único agente accede ahora a cientos de herramientas de la compañía simultáneamente.
- **La reconstrucción de CoCounsel Legal:** de habilidades separadas ejecutadas en secuencia al Claude Agent SDK, planificando y orquestando entre herramientas en tiempo real. Los datos de clientes siguen protegidos y fuera del entrenamiento de modelos de terceros.
- **Qué se prueba:** "Nuestra gran prueba para Claude es evaluar lo bueno que es haciendo planes y usando herramientas de forma eficaz."
- **Por qué Anthropic:** sus enfoques de transparencia, seguridad y desarrollo responsable de la IA; la primera prueba llegó con capacidades de investigación profunda construidas conjuntamente.
- **La postura a contracorriente sobre el retorno.** "Si intentas optimizar demasiado el cálculo de la tasa de retorno, los árboles no te dejan ver el bosque." Los cambios culturales de mentalidad van antes que las métricas de coste por tarea, aunque DORA y el tiempo hasta producción se siguen midiendo.
- **Una cifra concreta:** una herramienta interna de remediación de errores construida sobre Claude redujo el análisis de causa raíz de tres horas a cuatro minutos.
- **El trabajo mismo cambió.** "El acto de escribir líneas de código ya no es el trabajo": ahora pesan más el pensamiento sistémico, el criterio y el gusto, y el patrón hace a las personas "más en forma de T" a través de producto, diseño y finanzas.
- **Lo siguiente:** trabajo de horizonte más largo, mejor gestión del contexto y llamadas a herramientas fiables a lo largo de las cadenas de tareas del agente. Hron usa Claude Code para familiarizarse con bases de código y Claude Cowork para análisis estratégico.
- **El estándar:** la IA profesional tiene que funcionar en entornos "donde estar casi en lo cierto no es suficiente".

## Recursos incluidos
- `skills/defensible-ai-outputs/SKILL.md` — anclar el trabajo en contenido autorizado, validar citas antes de la revisión, cumplir los cuatro requisitos y comprobar transparencia, verificabilidad y defendibilidad.
- `skills/defensible-ai-outputs/references/four-requirements.md` — cada requisito, lo que implica en la práctica y lo que el post deja sin especificar.
- `skills/defensible-ai-outputs/templates/citation-validation-checklist.md` — una comprobación por afirmación y por resultado, más la entrega al profesional responsable.
- `skills/defensible-ai-outputs/examples/professional-workflows.md` — la investigación jurídica reconstruida en torno a la verificación, la redacción avanzada y la herramienta de remediación de errores.
- `skills/agent-first-product-rebuild/SKILL.md` — sustituir el encadenado que hace el usuario por un agente que planifica, exponer las herramientas ampliamente y probar los modelos en planificación y uso de herramientas.
- `skills/agent-first-product-rebuild/references/agent-architecture.md` — el antes y el después, lo que la arquitectura exige del modelo y las preguntas abiertas.
- `skills/agent-first-product-rebuild/references/measuring-the-shift.md` — la postura sobre el retorno, lo que se sigue midiendo y el cambio de fondo en el trabajo.
- `skills/agent-first-product-rebuild/templates/agent-readiness-review.md` — planificación, uso de herramientas, gestión del contexto y los cuatro requisitos profesionales, como registro.
- `skills/agent-first-product-rebuild/examples/cocounsel-rebuild.md` — la reconstrucción de CoCounsel Legal en detalle.
- `guides/building-ai-for-high-stakes-work.{en,ko,es,ja}.md` — el relato completo en cuatro idiomas.

## Fuente
[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Blog de Claude, 8 de julio de 2026.
