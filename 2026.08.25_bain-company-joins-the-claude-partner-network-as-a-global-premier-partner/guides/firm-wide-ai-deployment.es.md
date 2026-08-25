[English](./firm-wide-ai-deployment.en.md) · [한국어](./firm-wide-ai-deployment.ko.md) · **Español** · [日本語](./firm-wide-ai-deployment.ja.md)

# Desplegar IA en toda una firma

Una guía sobre la forma que debe tener un despliegue de IA a escala de toda una organización,
a partir de la implantación de Claude que Bain & Company hizo para sus 19.000 empleados,
anunciada cuando Bain se incorporó a la Claude Partner Network como socio Global Premier.

El anuncio es un anuncio de alianza, pero lo aprovechable está en el despliegue que describe.
Tiene cuatro propiedades que conviene copiar: se desplegó un **conjunto de superficies** y no
una sola herramienta; el piloto **produjo una cifra** antes del lanzamiento general; la
habilitación y la gobernanza salieron **junto con** el lanzamiento y no después; y el primer
objetivo de cara a cliente se eligió por dónde está realmente el cuello de botella.

## Desplegar un conjunto de superficies, no una herramienta

Claude llegó a los empleados a través de Claude.ai, Claude Cowork, Claude Code, Claude for
Excel y Claude for Microsoft 365.

Al recorrer esa lista se ve la lógica: una superficie de chat general, una de trabajo
agéntico, una de ingeniería, una de hoja de cálculo y la de documentos y correo que todo el
mundo tiene abierta todo el día. Tres de las cinco colocan el modelo **dentro** de una
herramienta que esa población ya usaba.

La única cifra de adopción por superficie que se reporta contiene la lección: más de dos
tercios de los participantes del piloto adoptaron Claude for Excel, la superficie incrustada
en la herramienta donde de verdad ocurre el trabajo analítico de una consultora.

La implicación para la planificación: mapee poblaciones a superficies **antes** de mapearlas
a licencias. Una ventana de chat entregada a toda una organización consigue la adopción de
quienes ya iban a adoptar.

## Haga que el piloto produzca una cifra

El dato reportado es que más de 7.000 empleados **usaban Claude activamente** a las pocas
semanas del despliegue en toda la firma.

Dos cosas importan más que su tamaño. Mide **uso activo**, no cuentas aprovisionadas. Y está
acotado a una ventana corta, lo que lo convierte en una afirmación sobre la **velocidad** de
adopción y no sobre su alcance final.

Diseñe el piloto para producir exactamente eso: una cohorte, una ventana y un recuento de
personas usando activamente cada superficie al cerrarla. Esa cifra es la que justifica la
decisión de disponibilidad general y contra la que se compararán todas las cohortes
posteriores.

## Publique habilitación y gobernanza con el lanzamiento

La implantación incluyó materiales de onboarding, sesiones de formación, webinars, soporte
experto y estructuras de gobernanza, con seguimiento de la experiencia de usuario mediante
encuestas continuas y recogida de feedback.

Trate esos cinco elementos como parte del lanzamiento, no como trabajo posterior. Un orden de
construcción práctico:

1. **Estructuras de gobernanza.** Reglas de datos enunciadas por superficie, una posición
   sobre qué puede usarse en trabajo de cara a cliente, un responsable nombrado para las
   decisiones sobre nuevas superficies y una vía de escalado. La gobernanza escrita después
   del lanzamiento es gobernanza escrita en respuesta a un incidente.
2. **Materiales de onboarding.** Una página por superficie, con una primera tarea específica
   del rol en lugar de un recorrido de funcionalidades, completable sin agendar tiempo con
   nadie.
3. **Sesiones de formación.** En vivo, segmentadas por rol, prácticas, usando el trabajo real
   de la organización como material de ejercicio. Repetidas para cada cohorte.
4. **Webinars.** Alcance y cadencia. Grábelos: la grabación se convierte en material de
   onboarding.
5. **Soporte experto.** Un canal atendido, enrutado por superficie. Su segunda función es
   diagnóstica: lo que llega repetidamente es el hueco de los puntos 2 y 3.

Y mantenga las encuestas en marcha. Una encuesta de lanzamiento mide el lanzamiento; una
recurrente le dice si la adopción se sostiene y qué superficie la está sosteniendo.

## Apunte al trabajo donde se ha perdido el contexto

El resultado de cliente reportado son ganancias de productividad del 30% al 50% en varios
proyectos con bases de código heredadas complejas, en concreto aquellas que carecen de
contexto arquitectónico.

Es un objetivo deliberado, no cómodo. Lo caro de ese trabajo no es el volumen: es que ya
nadie retiene la comprensión del sistema y hay que reconstruirla antes de poder cambiar nada.
Esa reconstrucción es justo aquello en lo que un modelo capaz de leer una base de código
entera resulta inusualmente bueno.

La regla transferible: elija el primer flujo de trabajo serio porque su cuello de botella es
el **contexto perdido**, no porque contenga mucho trabajo repetitivo. Los problemas de
rendimiento dan mejoras modestas y lineales. Las cifras grandes salen de los problemas de
recuperación de contexto.

## Presupueste la capacidad de despliegue

La alianza organiza el trabajo con clientes en tres áreas —estrategia de IA, modernización
tecnológica y operaciones habilitadas por IA— con más de 1.500 expertos en IA, datos,
analítica, arquitectura e ingeniería que trabajan junto a las prácticas sectoriales y de
capacidades de Bain.

Steve Corfield, responsable global de desarrollo de negocio de Anthropic, leyó la velocidad y
amplitud de la adopción de Bain como una señal de lo que se vuelve posible cuando la
tecnología se combina con la experiencia para desplegarla eficazmente. Philippe d'Arabian,
EVP y responsable global de alianzas de Bain, describió la alianza como la combinación de
tecnología de IA de frontera con experiencia estratégica y sectorial para convertir el
potencial de la IA en resultados de negocio.

La consecuencia de planificación es poco vistosa pero real: el insumo escaso no es la
capacidad del modelo, sino la **capacidad de despliegue**, y hay que dotarla de recursos
—desde dentro, desde un socio, o desde ambos.

## Fuente

- https://claude.com/blog/bain-company-joins-the-claude-partner-network-as-a-global-premier-partner (25 de agosto de 2026)
