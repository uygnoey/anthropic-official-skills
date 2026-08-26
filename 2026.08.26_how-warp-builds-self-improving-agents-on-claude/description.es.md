[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo Warp construye agentes que se automejoran sobre Claude

## ¿De qué trata este post?

Un caso de ingeniería de cliente. Warp —la terminal impulsada por IA y entorno de desarrollo
agéntico— comprobó que los agentes que operan con un 80% de precisión producen una experiencia
"ruidosa y molesta", y que reescribir prompts y archivos de contexto como `AGENTS.md` a mano no
escala como solución. El problema de fondo es que la retroalimentación humana desaparece cuando
termina la sesión.

Su respuesta es un bucle de dos skills: una skill base (interna) que hace el trabajo y una skill de
mejora (externa) que se ejecuta según un calendario, lee la retroalimentación humana acumulada y
propone ediciones pequeñas a la skill base como pull requests corrientes. El post explica cómo
escribir skills para ese bucle, recorre el agente de triaje de issues de Warp como ejemplo
trabajado y cierra con las preguntas que hay que responder antes de escalar el patrón.

## ¿Cuándo es útil?

- Uno de tus agentes acierta casi siempre pero es ruidoso, y reescribes su prompt a mano cada
  semana.
- Tienes retroalimentación de ingeniería sobre la salida del agente pero ningún mecanismo que la
  convierta en un cambio.
- Estás decidiendo cuántos bucles de mejora ejecutar: uno por agente o una plantilla compartida.
- Necesitas protegerte de que el agente actúe sobre retroalimentación simplemente equivocada.
- Quieres saber si tu dominio admite un arnés de verificación, y qué hacer si no.

## Puntos clave

- **El verdadero fallo es que la retroalimentación desaparece al terminar la sesión.** Reescribir
  prompts a mano y mejorar `AGENTS.md` no escala porque ataca el síntoma.
- **Skill interna / base.** Contiene el conocimiento funcional del dominio y las instrucciones, y se
  ejecuta sobre la tarea: en revisión de código, cuando se abre un PR.
- **Skill externa / de mejora.** Un observador que corre según un calendario, no por tarea. Recoge
  la retroalimentación humana acumulada, compara las sugerencias del agente con las respuestas de
  las personas y propone ediciones pequeñas y focalizadas a la skill base.
- **Las skills son archivos planos, así que las actualizaciones son PRs.** Los agentes proponen
  cambios mediante flujos que se revisan, aprueban y fusionan, lo que mantiene a las personas al
  mando de los cambios reales del sistema.
- **Escribe principios, no reglas; explica el porqué.** Instruye a una persona inteligente en vez de
  programar una computadora. La justificación permite razonar sobre situaciones nuevas y mejora la
  generalización.
- **Haz que dar retroalimentación no cueste nada.** Captúrala automáticamente donde la gente ya
  trabaja: comentarios en PRs e issues. "La baja fricción es lo que mantiene la señal fluyendo."
- **La retroalimentación explícita supera a la afirmación.** "Fue un comentario bueno y útil" vale
  menos que enunciar la convención y su razón.
- **La calidad supera al volumen, pero el volumen ayuda.** Una muestra pequeña de retroalimentación
  detallada y específica del dominio, de ingenieros senior, aporta señal que el agente no podía
  obtener de otra forma.
- **Invierte de más en la skill de mejora.** Es altamente reutilizable entre casos de uso.
- **El ejemplo trabajado.** El agente de triaje de Warp omitió la etiqueta `ready to spec`; una
  persona mantenedora explicó el porqué en la issue; la skill de mejora programada recuperó la
  retroalimentación reciente con un script de Python incluido, la resumió en JSON y propuso la
  edición más pequeña —aplicar `ready to spec` cuando una issue describe un problema real aunque el
  UI/UX esté sin definir—, que se integró como un PR revisado.
- **Antes de escalar, responde seis preguntas.** Skills frente a memoria, uno o varios bucles de
  mejora, qué hacer cuando la retroalimentación está equivocada, si el dominio es verificable, en
  qué apoyarse cuando no lo es, y qué métricas globales indican que el sistema completo mejora.

## Recursos incluidos

- `skills/self-improving-skill-loops/SKILL.md` — construir una skill base más una skill de mejora
  programada que la edita a partir de retroalimentación humana.
- `skills/self-improving-skill-loops/references/authoring-principles.md` — la guía de escritura del
  post, completa.
- `skills/self-improving-skill-loops/references/rollout-questions.md` — las seis preguntas de buenas
  prácticas y sus respuestas.
- `skills/self-improving-skill-loops/templates/improver-skill.md` — andamiaje para rellenar la skill
  externa.
- `skills/self-improving-skill-loops/scripts/collect_feedback.py` — implementación de referencia del
  paso de recolección de retroalimentación, con salida JSON.
- `skills/self-improving-skill-loops/examples/issue-triage-loop.md` — el bucle de triaje, paso a
  paso.
- `agents/skill-improver.md` — el agente observador programado.
- `agents/issue-triage.md` — el agente base de triaje al que mejora.
- `guides/self-improving-agent-loops.{en,ko,es,ja}.md` — el método completo en cuatro idiomas.

## Fuente

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (publicado el 2026-08-26)
