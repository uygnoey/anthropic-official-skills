[English](./working-with-a-frontier-model-in-cowork.en.md) · [한국어](./working-with-a-frontier-model-in-cowork.ko.md) · **Español** · [日本語](./working-with-a-frontier-model-in-cowork.ja.md)

# Trabajar con un modelo de frontera en Claude Cowork

Claude Fable 5 es el modelo más capaz de disponibilidad general de Anthropic, creado para trabajo
largo, complejo y asíncrono. Destaca especialmente ejecutando por su cuenta flujos de trabajo de
muchos pasos durante periodos prolongados: hacer una investigación a fondo que luego incorpora en un
primer borrador de memorándum, realizar la diligencia debida antes de generar presentaciones para el
consejo, o recorrer una carpeta para marcar cambios en varios contratos, comprobando y evaluando sus
resultados sobre la marcha.

Aprovecharlo al máximo exige cambiar la forma de trabajar con él. Las prácticas de siempre siguen
importando —buenas prácticas de prompting, aportar contexto, construir skills que capturen procesos
repetibles como las actualizaciones semanales del equipo, la preparación de llamadas comerciales o el
análisis del feedback de clientes—; de hecho, el modelo rinde aún mejor cuando ya están en su sitio.
Lo que cambia es que Fable 5 aplica tu contexto, tus preferencias y tus skills a lo largo de tareas
enteras, incluso las que tardan días, mientras que los modelos anteriores podían perder el hilo en
tramos largos y necesitaban recordatorios.

Trabajar con él se parece a trabajar con un colega muy competente: explicas la situación, acordáis
cómo es un buen resultado final y le dejas trabajar. Menos tiempo se te va en revisar cada paso, así
que más puede ir a decidir cuál debe ser el trabajo.

## Cómo complementa Fable 5 a Claude Cowork

Claude Cowork está hecho para producir trabajo terminado. Le das un objetivo y gestiona el resto,
incluso cuando la tarea es grande y compleja. Un encargo grande se divide en partes que corren a la
vez, cada una con su propio subagente: una instancia separada de Claude que toma una parte del trabajo
y reporta de vuelta. Así es como Claude atraviesa rápido grandes volúmenes de información. Cowork
también gestiona tareas grandes fijando un plan al inicio y contrastando sus propios resultados con él
mientras avanza.

Fable 5 saca amplia ventaja a los demás modelos de Anthropic en tareas largas y complejas, y las
tareas de Cowork suelen ser exactamente eso: decenas de pasos, cada uno apoyado en el anterior.

Piensa en construir el presupuesto del año que viene a partir de las cifras reales de este. Claude
accede a las hojas de cálculo y las lee, extrae las tasas de consumo, proyecta cada línea, concilia
las proyecciones con los objetivos y escribe el resumen. Si lee mal una tasa al principio, el error
fluye hacia todas las proyecciones siguientes. Fable 5 planifica el flujo antes de empezar y comprueba
resultados sobre la marcha, así que detecta la cifra mal leída mientras el trabajo corre y la corrige.

## Decidir cuándo usarlo

Fable 5 no es el modelo por defecto en Cowork: hay que seleccionarlo. En el momento de publicarse el
artículo, el predeterminado es Claude Sonnet 5, la elección correcta para las tareas cotidianas que tú
mismo resolverías en una pasada rápida. Claude Opus es una opción fiable para trabajo profundo con una
forma clara, donde ya sabes cómo es el resultado final. Fable 5 es para los proyectos que se sienten
más complejos o ambiguos, y que quizá quedaban fuera del alcance de modelos anteriores.

Dedica más tiempo a pensar y consume más de tus límites de uso, pero puede compensar en trabajo que
lleva mucho tiempo o que sale caro si se hace mal. La recomendación: reserva Fable 5 para tu trabajo
más importante, sobre todo los encargos que usan varias herramientas y exigen una serie de juicios.

**Esfuerzo.** Con un esfuerzo alto, Fable 5 planifica más antes de arrancar y comprueba más a lo largo
de la ejecución; mantén el esfuerzo alto en proyectos complejos o de muchos pasos que esperas que
Claude complete de principio a fin. Con esfuerzo bajo obtienes una respuesta más rápida sin renunciar
a la inteligencia de frontera; considéralo para tareas que necesitan criterio de frontera pero no
exploración profunda, como ejecuciones agénticas hechas de muchos pasos fáciles, o trabajo cuyo
resultado sea fácil de comprobar para Claude. En las pruebas de Anthropic, Fable 5 con esfuerzo bajo
igualó o superó con frecuencia a modelos anteriores en sus niveles máximos.

**Clasificadores.** Fable 5 llega con un nuevo conjunto de clasificadores: sistemas de IA
independientes que detectan posible uso indebido en solicitudes relacionadas con la ciberseguridad o
con la biología y la química. Cuando se activan, la respuesta pasa automáticamente a manos de Claude
Opus 4.8, y se informa al usuario cada vez que ocurre. Opus 4.8 es un modelo muy capaz por derecho
propio, y la conversación se queda en Opus a partir de ahí: hay que abrir una nueva para volver a
Fable 5. Estas salvaguardas se ajustaron de forma conservadora para poder lanzar un modelo de clase
Mythos de uso general con seguridad y rapidez, así que a veces atrapan solicitudes inofensivas,
incluidas frases en Cowork que solo rozan temas relacionados. Anthropic trabaja en reducir esos falsos
positivos.

## Empezar con apenas una idea

Cuando arrancas una tarea no siempre sabes qué intentas conseguir. Ese tramo inicial es donde Fable 5
puede ser un potente interlocutor, y en Cowork parte de tus skills, tus herramientas y tu
conocimiento.

Imagina que ves un anuncio relevante para tu sector o tu empresa. Puedes pedirle: *«Aquí tienes el
anuncio; dime qué cambia para nosotros, teniendo en cuenta todo lo que sabes de mi organización»*.
Lees la salida, empieza a formarse una estrategia y Claude construye un plan para producir los
materiales que necesitas, arrancando en la misma conversación donde ocurrió la lluvia de ideas.

Hacer lluvia de ideas en Cowork le da al modelo material real con el que pensar: puede leer los
archivos que has compartido y usar las herramientas que has conectado mientras habláis, de modo que
sus sugerencias son pertinentes. Detecta huecos en una idea cuando todavía es fácil cambiarla y te
muestra direcciones que no habías considerado. Y cuando la tarea empieza en esa misma conversación,
Fable 5 ya lleva consigo el objetivo que fijasteis, las restricciones que nombraste y las decisiones
que tomaste por el camino.

Una científica de datos de Anthropic llegó a Cowork con una idea para un nuevo panel de analítica
mientras el equipo aún decidía qué debía mostrar. Como Fable 5 pudo leer los datos de uso del equipo
durante la conversación, supo qué problemas tardan semanas en detectarse y clasificó las métricas que
los habrían pillado antes. Al final de la conversación tenía una lista corta de métricas que merecía
la pena añadir y un prototipo navegable.

Dos prompts que ayudan a convertir una idea en un resultado:

- **Pide a Claude que te entreviste:** «Antes de empezar, pregúntame todo lo que necesites saber para
  hacer esto bien».
- **Pide direcciones:** «Esto es más o menos lo que quiero. Dame tres formas de abordarlo, con una
  muestra rápida de cada una».

## Aporta contexto junto con tus restricciones

El contexto es la información con la que Claude trabaja; en Cowork son tu prompt, los archivos y
carpetas que hayas compartido y las herramientas que hayas conectado, como Asana, HubSpot, Jira, Slack
u otras.

Piensa en cómo informarías a un colega sobre un informe. No le entregarías una lista de reglas, pero
probablemente le dirías para quién es, para cuándo se necesita y qué tiene que conseguir, y confiarías
en que tome buenas decisiones a partir de ahí. Fable 5 funciona igual.

Las restricciones siguen siendo útiles: «que no pase de dos páginas y usa lenguaje llano» es una
instrucción perfectamente válida. Pero una restricción solo dice qué *no* hacer. El contexto dice para
qué *sirve* el trabajo, de modo que el modelo pueda acertar en situaciones que tus restricciones no
anticiparon.

Fable 5 maneja bien las tareas largas y de muchos pasos en parte por eso: cuando surge una pregunta o
un punto de decisión mientras trabaja, busca la respuesta en el contexto que compartiste. También usa
ese contexto para revisar su propio trabajo, así que dale algo concreto contra lo que juzgarse: un
borrador inicial de un informe y la versión final, y Claude deducirá tus estándares a partir de lo que
cambió entre ambos.

El contexto también le da una comprensión de tu situación, de forma que puede inferir o encontrar
detalles que nunca especificaste en el prompt, buscando en una base de conocimiento más amplia de la
que cabría en un prompt.

Una nota sobre las conversaciones con mucho contexto: para mantenerse al día, Claude vuelve a leer
toda la conversación con cada mensaje nuevo, así que un hilo largo puede consumir más uso. Conviene
empezar las tareas nuevas en una conversación nueva. Las tareas programadas también cuentan para tu
límite: revísalas de vez en cuando y desactiva las que ya no necesites.

## Delega encargos más grandes y complejos

Puede que estés acostumbrado a partir una tarea en trozos y a lanzar un prompt por cada uno. Fable 5
necesita muchos menos de esos prompts intermedios, así que puedes delegar encargos completos.

Sigue escribiendo tú los pasos cuando el proceso te importe, por ejemplo si una métrica tiene que
calcularse exactamente igual cada vez. Pero si lo que importa es el resultado, describe el objetivo y
deja que Claude haga el resto. Un prompt paso a paso puede limitarlo a los pasos que se te ocurrieron;
un objetivo le deja margen para encontrar un camino mejor.

Delegar en Cowork significa entregarle a Claude una decisión que normalmente tomarías tú. Tres formas
de hacerlo:

- **Delega el enfoque.** Dale el material y describe el resultado que quieres: *«Aquí está el feedback
  de clientes del último trimestre. Averigua por qué subieron las cancelaciones y qué deberíamos
  cambiar»*. Puede haber varias maneras razonables de recorrer esa carpeta, y la correcta depende de
  lo que haya en el feedback. Fable 5 lo lee todo, elige un enfoque y contrasta su conclusión con el
  feedback antes de traértela. Puedes juzgar la respuesta sin especificar cómo llegó a ella.
- **Delega el procedimiento.** Una skill le enseña a Claude un procedimiento que usa tu equipo: cómo
  construís un informe, formateáis una presentación, ejecutáis un análisis. No hace falta decirle qué
  skills usar ni en qué orden. Di *«prepara la revisión trimestral como siempre la hacemos»* y Fable 5
  elige las skills adecuadas en el momento adecuado.
- **Delega el calendario.** Para trabajo que quieras repetir, describe el resultado y Claude montará
  el calendario y lo convertirá en una tarea recurrente: *«Quiero empezar cada lunes sabiendo qué
  cambió en el pipeline y qué necesita una decisión»*.

Llévale a Fable 5 trabajo más difícil del que sueles darle a una IA, incluso trabajo que dabas por
imposible: desordenado o poco claro, o que puede llevar horas o días. Descríbelo y comprueba si el
modelo puede trabajar a ese nivel. Elige un resultado del que seas responsable, di cómo lo juzgarías y
deja que Claude proponga los pasos para llegar. Parte de ese trabajo puede convertirse en una tarea
programada que corra sola; Claude puede guardar el procedimiento como skill y ponerlo en un
calendario, trabajando a través de las herramientas que ya tienes conectadas.

## Revisa el proceso de pensamiento de Claude

Parte de lo que permite a Fable 5 sostener trabajo largo es que sabe fijar y seguir un plan. En Cowork
puedes ver ese plan mientras trabaja: el panel junto a la conversación enumera lo que pretende hacer y
después los archivos que lee y escribe y las herramientas y skills que usa.

Ese panel es tu oportunidad de detectar problemas y redirigir pronto. Un error que de otro modo
encontrarías en el resultado final aparece aquí como un paso equivocado en el plan. Corriges el plan
en una frase y Claude se ajusta sin empezar de cero.

Cuando el trabajo termine, revísalo como revisarías el de un colega: abre los archivos que produjo y
léelos. Si algo no cuadra, el registro de la ejecución sigue en la conversación. Repasa los pasos que
Claude fue listando mientras trabajaba, incluidos los archivos que leyó y las herramientas que usó, y
despliega su razonamiento para ver por qué tomó una decisión. O pregúntale directamente: *«¿De dónde
sale esta cifra?»*, y Claude te señalará la fuente.

Empieza con trabajo que sepas verificar, como el primer borrador del plan del próximo trimestre para
tu equipo. Si conoces bien las prioridades, sabrás enseguida si la pasada de Claude se sostiene.
Delega encargos mayores conforme los resultados demuestren ser fiables.

## Invierte en tu configuración de Cowork

Un modelo más capaz eleva el valor de cada conexión que has hecho, desde las carpetas que has
compartido hasta las herramientas en las que trabaja tu equipo.

**Conecta tus herramientas.** Empieza por las que usas a diario: correo, calendario, documentos, el
chat de tu equipo. Cada conexión amplía lo que Claude puede hacer sin que tú copies nada. Fable 5 es
bueno decidiendo cuándo merece la pena usar una herramienta: con tus herramientas conectadas, se da
cuenta de que la respuesta está en tu calendario o en un hilo de chat y va a buscarla, en vez de
esperar a que se lo indiques.

**Ajusta la escritura a tu voz.** Cada modelo nuevo llega con sus propios valores por defecto de
escritura: voz, extensión y las expresiones a las que recurre primero. Fable 5 tiene los suyos, como
un estilo más escueto o difícil de seguir en sesiones largas. Voz, tono y estilo se personalizan
fácilmente mediante prompts o en las instrucciones del proyecto; por ejemplo, «usa un lenguaje llano,
directo y sencillo». Si usas memoria, revisa de vez en cuando qué ha guardado Claude sobre tus
preferencias de escritura. Para documentos donde quieras una voz concreta, usa conectores o archivos
existentes para que Claude repase tus textos anteriores y guarde lo que encuentre como una skill a la
que recurrir la próxima vez. Fable 5 sigue las instrucciones permanentes más de cerca que modelos
anteriores y aprovecha mejor el material guardado cuando hace falta.

**Revisa lo que configuraste para modelos anteriores.** Las instrucciones guardadas —skills y archivos
de memoria— escritas para un modelo anterior suelen arrastrar correcciones que aquel modelo
necesitaba. Trasladadas tal cual, esas correcciones antiguas pueden limitar a un modelo nuevo. Pide
una auditoría: *«Repasa mis skills y mi memoria guardada. ¿Cuáles siguen encajando y cuáles se
escribieron para un modelo antiguo?»*

## Lo que viene

A medida que la inteligencia de frontera siga evolucionando, Claude Cowork será cada vez más capaz,
permitiendo trabajo aún más prolongado y desbloqueando más casos de uso de trabajo del conocimiento.
Aprender a hacer prompting, gestionar el contexto, comprobar el trabajo de Claude y delegar tareas te
ayudará a aprovechar todo lo que Fable 5 y los modelos futuros tienen que ofrecer.

## Fuente

[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork)
— Josefina Albert, equipo de Educación de Anthropic, 16 de julio de 2026.
