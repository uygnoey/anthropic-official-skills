[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Una guía sobre la anatomía de los agentes de comercio eficaces

## ¿De qué trata este post?

Una guía de ingeniería extensa, de Ali Shazal y Matthew Koen, destilada del trabajo de Anthropic
con equipos empresariales de retail, marketplaces, viajes, entretenimiento y telecomunicaciones.
Recorre la construcción de un agente de comercio en producción en cuatro partes: la arquitectura,
cómo hacerlo rápido y asequible, cómo operarlo en producción, y qué sigue siendo cierto cuando
cambian los modelos.

La afirmación central es arquitectónica: un agente de comercio debe ser **un modelo en un bucle
de agente estándar**, con agent skills para la modularidad, no una flota de subagentes. Las
conversaciones de comercio permanecen fuertemente acopladas entre intenciones y turnos, así que
cada traspaso a un subagente pierde estado, multiplica el coste en tokens y añade latencia. Un
solo agente con skills ha superado consistentemente en calidad tanto al diseño de
un-prompt-para-todo como al de subagentes, y con frecuencia a menor coste y latencia por tarea.

## ¿Cuándo es útil?

- Estás diseñando un agente de compras o de comerciante y debes decidir cómo descomponerlo.
- Tu agente funciona pero es demasiado lento, o cuesta demasiado por tarea, y necesitas saber qué
  palanca tocar primero.
- Necesitas memoria a largo plazo entre sesiones sin pagar latencia por ella en cada turno.
- Tu agente puede tocar carritos, pedidos, precios, reembolsos o presupuestos, y necesitas una
  aplicación que no dependa de que el modelo se comporte.
- Estás construyendo una suite de evals para un sistema no determinista que varios equipos
  modifican a la vez.

## Puntos clave

- **Skills, no subagentes.** Los traspasos pierden estado, multiplican el coste y añaden
  latencia, y las fronteras de dominio del comercio no se separan limpiamente. Reserva los
  subagentes para tareas estrechas y autocontenidas como la investigación profunda, o para un
  dominio que ya opera su propio agente sujeto a cumplimiento.
- **La ubicación se decide por frecuencia.** Prompt de sistema para lo necesario en la mayoría de
  los turnos (en torno a un tercio del tráfico o más); skills para la cola larga. Lo relativo a
  seguridad, legal, marca y seguridad del usuario va al prompt de sistema pase lo que pase.
- **Las herramientas llaman a sistemas que ya operas.** La frontera de la herramienta es donde
  acaba su lógica y empieza el juicio del modelo. Reformatea la respuesta cruda dentro de la
  herramienta y devuelve orientación accionable ante errores, no códigos de error.
- **Los componentes de interfaz son herramientas.** `present_products`, `present_itinerary` —
  almacenamiento nativo en el array de mensajes, seguridad de tipos, layout referenciable ("el
  tercero de arriba"), streaming progresivo. Los argumentos se acumulan en el servidor;
  `eager_input_streaming: true` cambia parte de la garantía de esquema por streaming a nivel de
  token.
- **Latencia = (turnos × tiempo hasta el último token) + tiempo de herramientas.** Menos turnos,
  herramientas más rápidas, tokens más rápidos. Precarga contexto, deja que la inteligencia
  recupere turnos, habilita llamadas paralelas y despacha de forma temprana.
- **La latencia percibida es otro problema.** Transmite los componentes progresivamente y muestra
  líneas de progreso cortas construidas desde los argumentos de la herramienta o un parámetro
  `user_facing_message`.
- **La caché de prompts es la mayor palanca de coste.** Tres segmentos por frecuencia de cambio —
  global (idéntico byte a byte), sesión, volátil (al final). Carga las skills como resultados de
  herramienta y haz avanzar los puntos de corte. Los mejores despliegues operan al 90-99% de
  aciertos.
- **Elige el modelo con un barrido.** Define métricas de calidad, latencia y coste, ejecuta la
  suite completa de evals sobre modelos y niveles de esfuerzo, reajusta los prompts por modelo y
  mide el coste por tarea. Si está parejo, elige inteligencia.
- **Escribe la memoria de forma asíncrona, fuera del agente.** Un proceso aparte lee la
  conversación y crea, actualiza o borra hechos tipados: sin coste de latencia y un 13% más de
  recuperación de hechos en evals internos. El extractor lee solo texto de usuario y asistente,
  nunca resultados de herramienta.
- **Lee la memoria en tres capas.** Siempre en contexto, precargada por turno, y detrás de una
  herramienta de consulta.
- **La aplicación de la seguridad vive en el arnés.** El modelo prepara y una persona o política
  aplica; las escrituras y renders solo aceptan IDs emitidos por el servidor; los topes se aplican
  sobre el estado resultante con escrituras serializadas por sesión; todo el contenido de terceros
  se sanea, y el texto dentro de la cerca es reportable, nunca accionable.
- **Evals de snapshot, no simulación de conversación.** Construye el estado directamente y
  califica el estado final y la respuesta. Las ejecuciones con usuario simulado sirven solo para
  descubrir cobertura. Parte de historiales largos, desordenados y contradictorios: ahí viven los
  fallos emergentes.
- **Publica con propiedad clara y una suite de CI selectiva.** Casos básicos de alto tráfico, más
  todos los de seguridad, más los que toca el cambio. El agente es una única unidad de
  despliegue: hazle canario y ponlo en el calendario de releases.

## Recursos incluidos

- `skills/commerce-agent-architecture/SKILL.md` — el diseño de un agente con skills, la regla de
  ubicación, la ingeniería de herramientas y los componentes de interfaz como herramientas.
- `skills/commerce-agent-architecture/references/skills-vs-subagents.md` — la contrapartida
  completa y los dos casos donde el subagente sigue encajando.
- `skills/commerce-agent-architecture/references/capability-map.md` — el reparto prompt/skill de
  la implementación de referencia para agentes de compras y de comerciante.
- `skills/commerce-agent-architecture/references/ui-components-as-tools.md` — beneficios, la
  contrapartida del buffering y `eager_input_streaming`.
- `skills/commerce-agent-latency-and-cost/SKILL.md` — las tres palancas de latencia, la latencia
  percibida, la caché y la selección de modelo.
- `skills/commerce-agent-latency-and-cost/references/prompt-cache-segments.md` — la disposición en
  tres segmentos y una lista de comprobación.
- `skills/commerce-agent-latency-and-cost/references/model-selection-sweep.md` — el procedimiento
  del barrido y el criterio de desempate.
- `skills/commerce-agent-memory/SKILL.md` — registros tipados, extracción asíncrona, las tres
  capas de lectura.
- `skills/commerce-agent-memory/templates/memory-fact-record.json` — la forma del registro.
- `skills/commerce-agent-memory/references/memory-data-handling.md` — retención, corrección,
  borrado, interruptor por despliegue.
- `skills/commerce-agent-safety-harness/SKILL.md` — los cuatro principios de aplicación.
- `skills/commerce-agent-safety-harness/references/safety-principles.md` — cada principio en
  detalle.
- `skills/commerce-agent-safety-harness/scripts/sanitize_untrusted_content.py` — un saneador
  ejecutable para listados, reseñas, políticas, mensajes de vendedores y memoria almacenada.
- `skills/commerce-agent-evals/SKILL.md` — pruebas de snapshot y las cinco áreas de cobertura.
- `skills/commerce-agent-evals/references/eval-coverage-matrix.md` — la matriz completa de casos.
- `skills/commerce-agent-evals/references/ci-suite-selection.md` — propiedad, selección de CI y
  prácticas de calendario de releases.
- `skills/commerce-agent-evals/templates/snapshot-case.md` — un caso de snapshot para rellenar.
- `guides/anatomy-of-a-commerce-agent.{en,ko,es,ja}.md` — la guía completa en cuatro idiomas.

## Fuente

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (publicado 2026-09-02)
