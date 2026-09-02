[English](./anatomy-of-a-commerce-agent.en.md) · [한국어](./anatomy-of-a-commerce-agent.ko.md) · **Español** · [日本語](./anatomy-of-a-commerce-agent.ja.md)

# La anatomía de un agente de comercio eficaz

Una guía destilada del trabajo de Anthropic con equipos empresariales de retail, marketplaces,
viajes, entretenimiento y telecomunicaciones. Cubre cuatro cosas en orden: la arquitectura, cómo
hacerlo rápido y asequible, cómo operarlo en producción, y qué sigue siendo cierto cuando
cambian los modelos.

## Parte 1 — La arquitectura

### Qué es un agente de comercio

Los agentes de comercio simplifican comprar y vender a través de catálogos en línea. Las
variantes orientadas al consumidor manejan búsqueda, comparación, sustitución y armado de
pedidos. Las orientadas al negocio manejan analítica de ventas, promociones, inventario y
precios. Por debajo, ambas son el mismo diseño: **un modelo en un bucle de agente estándar —
razonando sobre un objetivo, explorando contexto, actuando a través de herramientas.**

### Skills, no subagentes

La guía es tajante: no descompongas un agente de comercio en subagentes.

- Las conversaciones de comercio permanecen fuertemente acopladas a lo largo de múltiples
  intenciones y turnos.
- Los traspasos entre subagentes producen pérdida de estado, que degrada la calidad de la
  respuesta.
- Cada traspaso multiplica el coste en tokens y añade latencia.
- Las fronteras de dominio no se separan limpiamente en los flujos de comercio.

Las agent skills dan modularidad sin el sobrecoste del traspaso. En palabras de la guía, un solo
agente con skills *"ha superado consistentemente tanto al diseño de un-prompt-para-todo como al
diseño de subagentes en calidad, y con frecuencia a menor coste y latencia por tarea."*

Los subagentes conservan su valor solo en dos casos: una tarea estrecha y autocontenida como la
investigación profunda, o un dominio que ya opera su propio agente dedicado con sus propios
requisitos de cumplimiento.

### ¿Prompt de sistema o skill? Decide por frecuencia

- **Prompt de sistema** — contenido necesario en la mayoría de los turnos, aproximadamente un
  tercio del tráfico o más.
- **Skills** — funcionalidades de cola larga y capacidades condicionales.

Las instrucciones críticas son la excepción y viven siempre en el prompt de sistema: reglas de
seguridad, requisitos legales, restricciones de marca y hechos relativos a la seguridad del
usuario.

La implementación de referencia se reparte así:

- **Prompt del agente de compras:** grounding, semántica de carrito y checkout, reglas de
  presentación, búsqueda de productos.
- **Skills de compras:** search-discovery, purchase-research, planning-goals, customer-care,
  memory-personalization.
- **Skills de comerciante:** performance-insights, catalog-listings, inventory-operations,
  pricing-promotions, marketing-campaigns.

### Ingeniería de las herramientas

**Construye sobre los sistemas existentes.** Las herramientas del agente deben llamar al
catálogo, al carrito, al motor de precios y al sistema de pedidos que ya operas — *"no
reimplementarlos; la frontera de la herramienta es donde termina su lógica y empieza el juicio
del modelo."*

**Los resultados de herramienta son contexto.** Devuelve solo los campos relevantes para razonar.
*"Reformatea la respuesta cruda dentro de la herramienta, incluyendo añadir un siguiente paso
cuando no sea obvio a partir de los datos."* Ante errores, devuelve orientación accionable en
lugar de un código de error.

### Componentes de interfaz como herramientas

En lugar de marcado propio, convierte cada componente de interfaz en una herramienta —
`present_products`, `present_itinerary`. Obtienes componentes almacenados en su formato nativo en
el array de mensajes, seguridad de tipos y validación, el layout preservado para que el usuario
pueda decir "el primer hotel" o "el tercero de arriba", y streaming progresivo al cliente.

La contrapartida es que los argumentos de las herramientas de presentación se acumulan en el
servidor, lo que afecta a la latencia percibida. Activar `eager_input_streaming: true` habilita
streaming a nivel de token con garantías de esquema reducidas; la guía señala que las violaciones
de esquema son *"muy raras en modelos de clase Claude Sonnet en adelante."*

## Parte 2 — Rápido y asequible

### Latencia de finalización de tarea

```
(turnos de modelo × tiempo hasta el último token) + procesamiento de herramientas
```

De esa forma salen tres palancas:

1. **Menos turnos** — precarga el contexto probable, usa un modelo más capaz, habilita llamadas
   paralelas a herramientas.
2. **Herramientas más rápidas** — optimiza los backends, despacha las herramientas de forma
   temprana.
3. **Tokens más rápidos** — elige modelo y configuración mediante un barrido de evals.

En la práctica: inyecta la página de producto o el panel desde el que llegó el usuario; recuerda
que los modelos más inteligentes reducen el número de turnos en consultas complejas y eso suele
compensar una velocidad por token menor; deja que el modelo llame a varias herramientas por
turno, porque el comercio necesita constantemente búsquedas múltiples, consultas de políticas y
lecturas de datos simultáneas; y ejecuta cada herramienta en cuanto sus argumentos terminan de
transmitirse, lo que convierte huecos de varios segundos en cientos de milisegundos.

### Latencia percibida

Independiente de la duración real:

- **Transmite los componentes progresivamente.** Divide una respuesta de 500-700 tokens en
  renderizados progresivos.
- **Muestra el trabajo.** Una línea de progreso corta por paso — "buscando hoteles cerca del
  agua" — construida a partir de los argumentos de la herramienta o de un parámetro
  `user_facing_message` dedicado.

### Caché de prompts

La mayor reducción de coste disponible.

- Una lectura de entrada cacheada cuesta una décima parte de un token nuevo.
- Las escrituras de caché llevan una prima de ~1,25x que se recupera en el segundo uso.
- *"Los mejores despliegues de comercio que hemos visto operan con tasas de acierto de caché del
  90-99%."*
- Los tokens cacheados también aportan una mejora de velocidad de ~1,5-2x en torno a los 100k
  tokens.

Estructura el contexto en tres segmentos, ordenados por frecuencia de cambio:

1. **Global** — prompt de sistema y definiciones de herramientas, idénticos byte a byte entre
   sesiones.
2. **Sesión** — contexto por usuario e historial de conversación.
3. **Volátil** — hora actual, página actual. Debe aparecer al final del segmento.

Dos detalles de implementación importan. Carga las skills como **resultados de herramienta**, no
como apéndices del prompt de sistema, para que caigan en el prefijo conversacional cacheado. Haz
avanzar los puntos de corte de caché en cada turno para mantener la coincidencia del prefijo. Y
cuando una señal como el contexto de página te dice qué skill hará falta, inyéctala desde el
principio y ahórrate el turno de carga.

### Elegir modelo y configuración

1. **Define métricas** — umbrales de calidad (finalización de tarea, relevancia, grounding),
   latencia (p50/p99), presupuestos de coste.
2. **Barre** — ejecuta la suite completa de evals sobre modelos y niveles de esfuerzo candidatos.
3. **Itera** — los prompts se afinan a modelos concretos; los modelos pequeños necesitan
   instrucciones explícitas que los grandes infieren.
4. **Mide el coste por tarea** — contabiliza el número de turnos y las tasas de fallo, no solo el
   coste por llamada.

> Cuando el resultado es parejo, y el coste encaja en tu economía por tarea y tu latencia, elige
> inteligencia.

## Parte 3 — Operar en producción

### Memoria que sobrevive a la sesión

Los usuarios no deberían repetir restricciones — alergias, preferencias — en cada sesión.

**Almacenamiento.** La memoria pertenece a bases de datos de producción, no al contexto del
modelo. Estructura los hechos como registros tipados: clave (`shoe_size`, `default_store`),
valor, categoría, sesión de origen.

**Tratamiento de datos.** Decide qué tipos de memoria conservar y aplícalo en la ruta de
escritura con un validador. Ofrece interfaces para que el usuario vea, corrija y borre los hechos
almacenados. Fija periodos de retención, porque las preferencias caducan. Haz de la memoria un
interruptor por despliegue para el cumplimiento jurisdiccional.

**Escritura.** Usa extracción asíncrona en lugar de una herramienta del agente. *"Escribe la
memoria de forma asíncrona... al final de cada turno, o cada pocos turnos... Un agente en un hilo
o proceso separado lee la conversación y crea, actualiza o borra hechos."* Esto elimina el
sobrecoste de latencia, logró un 13% más de recuperación de hechos en evals internos, y quita
carga de decisión al razonamiento del agente. El prompt de extracción debe leer solo texto de
usuario y de asistente, nunca resultados de herramienta — de lo contrario las descripciones de
producto se convierten en hechos del usuario.

**Lectura, en tres capas.**

1. **Siempre en contexto** — hechos fijos que casi toda petición necesita, como tienda por
   defecto y preferencia de entrega.
2. **Precargados por turno** — hechos que las señales de la petición actual vuelven relevantes.
3. **Herramienta de consulta** — todo lo demás, detrás de una recuperación explícita.

### Seguridad: la aplicación vive en el arnés

El prompt inicia el comportamiento seguro; el código lo aplica. Los cuatro principios valen igual
para agentes de consumidor y de comerciante.

1. **El modelo prepara; una persona o una política aplica.** Ninguna herramienta del agente mueve
   dinero ni cambia el estado del negocio directamente. Colocación de pedidos, pagos,
   reembolsos, cambios de precio y campañas requieren aprobación aguas abajo a través de los
   flujos de aprobación existentes.
2. **Las escrituras y los renders solo aceptan IDs emitidos por el servidor.** Mantén un
   inventario por sesión de IDs emitidos por el servidor. El agente no puede usar IDs
   alucinados, pegados por el usuario ni provenientes del plano de datos. Las herramientas de
   presentación renderizan solo registros suministrados por el servidor.
3. **Las transacciones con tope resisten peticiones repetidas.** Aplica el tope sobre el estado
   resultante, no sobre la petición. Serializa las escrituras del carrito por sesión para que
   llamadas paralelas no acumulen por encima del límite. Aplica la misma lógica a los cambios del
   comerciante — topes de variación de precio, profundidad de descuento, presupuesto.
4. **El contenido de terceros se sanea.** Toda entrada no confiable — listados, reseñas,
   políticas, mensajes de vendedores, memoria almacenada — pasa por un saneador antes de llegar
   al modelo. Elimina caracteres de control, quita imitaciones de los marcadores de cerca,
   desactiva la imitación de conversación y de llamadas a herramientas, y limita el tamaño. El
   prompt lleva la instrucción correspondiente: el texto dentro de la cerca es reportable, nunca
   accionable.

### Evals: publicar un sistema no determinista

**Pruebas de snapshot, no simulación de conversación.** Construye el estado de prueba
directamente — prompt de sistema, herramientas, array de mensajes —, añade el mensaje de usuario
de prueba, ejecuta el agente y califica el estado final y la respuesta. *"Los evals con usuario
simulado... son una herramienta pobre para medir"* porque la complejidad de la interacción exige
muestras mayores. Úsalos para descubrir cobertura y convierte los hallazgos en casos de snapshot.

**Prueba condiciones difíciles.** La mayoría de las suites sobrepondera los casos de estado
limpio. *"Asegúrate de que una parte de los tuyos parte de historiales largos, desordenados o
contradictorios"* — ahí es donde afloran los fallos emergentes.

**Cobertura.** Peticiones básicas; peticiones dependientes del contexto; casos de seguridad y
marca; evaluación de la interfaz; y peticiones multicapacidad donde hacen falta dos capacidades
vecinas a la vez y se califican ambas mitades.

**Prácticas.** Colabora con expertos de Producto, Legal, Operaciones, Atención y Categoría. Los
casos de mayor valor salen de fallos reales en producción. Empieza con 50-100 casos por flujo de
usuario. Usa Claude Code para generar casos y variantes adversarias.

### Publicar en organizaciones grandes

1. **La propiedad sigue a los sistemas.** Cada skill y herramienta tiene un único equipo
   propietario; el prompt compartido tiene un propietario a nivel de plataforma más propietarios
   de dominio. Añadir una skill incluye aportar casos positivos, negativos y de frontera.
2. **Los cambios se publican con casos; CI ejecuta una suite selectiva.** Construye el conjunto
   de CI con los casos básicos de alto tráfico, todos los casos de seguridad, y los casos que
   toca el cambio. Para una skill: sus propios casos más los casos frontera de las vecinas. Para
   una herramienta: todos los casos que la llaman. Para el prompt compartido: la suite completa.
3. **Mete al agente en el calendario de releases.** Es una única unidad de despliegue, así que un
   cambio malo llega a todos a la vez. Despliegue canario para cambios de prompt y skills,
   interruptores para desactivar sin desplegar, y congelación antes de los periodos pico.

## Parte 4 — Lo que sigue siendo cierto

> La mayor parte de lo que describe este post no va del modelo. Las herramientas llaman a
> sistemas que ya operas, las skills codifican procedimientos que ya sigues, los evals son tu
> documento de requisitos de producto escrito como pruebas.

Por delante: interfaces de voz, comportamiento proactivo del agente como vigilar bajadas de
precio, y abrir las herramientas a agentes de terceros bajo los mismos marcos de preparación,
aprobación y procedencia.

## Implementación de referencia

Anthropic publica un repositorio blueprint en
[github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) con
arneses y patrones, guardarraíles de seguridad y cumplimiento, implementaciones de referencia de
agentes de compras y de comerciante, ejemplos de retail, viajes, telecomunicaciones y ticketing,
y un plugin de Claude Code para escribir evals.

## Fuente

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (publicado 2026-09-02)
