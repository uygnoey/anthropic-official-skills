[English](./self-improving-agent-loops.en.md) · [한국어](./self-improving-agent-loops.ko.md) · **Español** · [日本語](./self-improving-agent-loops.ja.md)

# Bucles de agentes que se automejoran: cómo lo hace Warp

## El problema

Warp —la terminal impulsada por IA y entorno de desarrollo agéntico— comprobó que los agentes que
ejecutan tareas con un 80% de precisión generan una experiencia de usuario "ruidosa y molesta".
El equipo se topó con esto en su propio agente interno de revisión de código: los ingenieros
reportaban comentarios poco útiles y salidas de baja calidad.

Las soluciones evidentes no escalaban. Reescribir prompts a mano y mejorar archivos de contexto
como `AGENTS.md` es trabajo que nunca termina. El problema real está un nivel más abajo: **la
retroalimentación normalmente desaparece cuando termina la sesión**, y con ella se pierde el
contexto esencial del bucle agéntico.

## El marco de trabajo

La solución de Warp se apoya en **skills** —conocimiento codificado en archivos— con dos
componentes y las personas en medio.

### Skill interna / base

Contiene el conocimiento funcional del dominio y las instrucciones. En revisión de código, se
ejecuta cuando se abre un PR y produce la revisión.

### Retroalimentación humana

El ingrediente crítico. La retroalimentación explícita funciona mejor: explicar no solo qué estuvo
mal, sino *por qué*. Como lo plantea Zach Lloyd, CEO de Warp: una persona puede confirmar "este fue
un comentario bueno y útil", pero razones detalladas como "la convención de nuestro código es que
este tipo de variable global usa este contexto de nombres" son las que le dicen al agente cómo
mejorar.

### Skill externa / de mejora

Un agente observador que se ejecuta **según un calendario**, no por tarea. Recoge la
retroalimentación humana acumulada, compara las sugerencias del agente con las respuestas de las
personas y propone ediciones pequeñas y focalizadas a la skill base.

Como las skills son archivos planos, los agentes las actualizan a través de flujos de PR que se
pueden revisar, aprobar y fusionar. Nada cambia en el sistema en producción sin que una persona
haga el merge.

## Cómo escribir skills que se automejoran

- **Escribe principios, no reglas.** Instruye a una persona inteligente, no programes una
  computadora. "Busca código repetido" da mejor dirección que un reglamento exhaustivo de nombres
  de variables.
- **Explica el porqué.** La justificación permite que el agente razone sobre los problemas en vez
  de seguir instrucciones rígidas, lo que mejora la generalización.
- **Haz que dar retroalimentación no cueste nada.** Captúrala donde la gente ya trabaja —
  comentarios directos en el PR o en la issue— de forma automática, sin un paso de envío adicional.
  La baja fricción es lo que mantiene la señal fluyendo: si lo pones difícil, la retroalimentación
  se corta y la mejora también.
- **Mantén las skills pequeñas y usa divulgación progresiva.** Un buen archivo de skill referencia
  archivos de recursos y scripts en lugar de volcarlo todo al contexto de una vez.
- **La calidad de la retroalimentación supera al volumen, pero el volumen ayuda.** La
  retroalimentación detallada y específica del dominio de ingenieros senior pesa más que la
  superficial. Incluso una muestra pequeña da muy buena señal cuando aporta conocimiento de dominio
  que el agente no tenía forma de obtener.
- **Invierte esfuerzo extra en la skill de mejora.** Rinde dividendos, porque las skills de mejora
  son altamente reutilizables entre casos de uso.

## El bucle en acción: triaje de issues

El [agente de triaje de issues](https://github.com/warpdotdev/warp-agents-demo-github-issue-triage)
de Warp demuestra el marco de principio a fin.

1. Alguien abre una issue en GitHub. Una GitHub Action dispara el agente, que analiza complejidad y
   viabilidad, asigna etiquetas y sugiere una dirección para la corrección.
2. En una issue de muestra la skill interna funcionó bien pero omitió la etiqueta `ready to spec`,
   la que indica que quienes contribuyen pueden construir las especificaciones de producto y
   técnicas.
3. Una persona mantenedora dejó retroalimentación directamente en la issue, explicando tanto la
   expectativa como su justificación.
4. La skill externa de mejora, ejecutándose en Oz —la plataforma de orquestación de Warp— como un
   agente programado "update triage", se autenticó en GitHub, ejecutó un script de Python incluido
   para recuperar las issues recientes con retroalimentación, resumió los hallazgos en JSON e
   identificó señales concretas.
5. Propuso la edición más pequeña que capturaba la retroalimentación: aplicar `ready to spec`
   cuando una issue describe un problema real aunque los detalles de UI/UX estén sin definir.
6. La actualización pasó por el flujo estándar de revisión de código. El PR explicaba qué señales
   motivaron qué cambios. Tras la aprobación humana, el cambio fusionado se convirtió en
   conocimiento heredado para la siguiente ejecución del triaje.

Warp hoy aplica este patrón en todo su repositorio de código abierto, con agentes separados de
escritura de especificaciones, revisión y triaje, cada uno con su propio bucle de automejora.

## Preguntas que responder antes de escalar

**¿Estás confundiendo skills con memoria?** Las skills son procedimentales y estables —"cómo hacer
X"—, independientes de la ejecución y se cambian deliberadamente. La memoria la escriben los
agentes automáticamente en tiempo de inferencia y cambia constantemente.

**¿Un bucle de mejora, o uno por agente?** Encuéntrate en el medio: un bucle base plantillado
captura lo que se solapa entre agentes, con pesos específicos del dominio encima. Un puñado de
agentes puede tener cada uno el suyo; cien deberían compartirlo.

**¿Qué pasa cuando la retroalimentación está equivocada?** Asume que lo estará. No dejes que los
agentes la acepten a ciegas: dales contexto para verificarla, filtra de quién cuenta la opinión y
mantén a las personas en el bucle en la etapa de filtrado, en la de revisión final, o en ambas.

**¿Tu dominio es verificable?** Construye primero el arnés de verificación y luego deja que el
agente se ajuste contra él: genera un corpus de referencia, compara la salida con la referencia,
corrige, repite.

**¿Y si no lo es?** Apóyate en evaluaciones deterministas contra salidas de referencia allí donde
existan. Donde la retroalimentación humana sea necesaria, restríngela a personas expertas en el
dominio; no abras las compuertas.

**¿Cómo sabes que el sistema completo está mejorando?** Sigue las métricas globales que las
personas ya monitorean —tiempo hasta el merge, número de contribuyentes, coste— y realiméntalas a
los agentes de mejora. Avanza gradualmente de gatear a caminar y a correr en el despliegue.

## Sobre Warp

Fundada en 2020 por su CEO Zach Lloyd. Stack: Rust, Golang, GitHub Actions, una plataforma interna
de orquestación de agentes llamada Oz y la Claude Platform. 73 millones de dólares levantados,
800 000 desarrolladores mensuales, 56% de las Fortune 500, 10 millones de sesiones de Claude Code
ejecutadas dentro de Warp hasta la fecha (más de 400 000 por semana) y 40 millones de
conversaciones totales con Warp Agent.

## Fuente

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (publicado el 2026-08-26,
  por Michael Segner)
