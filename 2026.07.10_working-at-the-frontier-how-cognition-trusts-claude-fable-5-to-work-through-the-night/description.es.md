[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Silas Alberti, SVP de Investigación en Cognition, ha probado casi todos los modelos de Claude dentro de Devin, el ingeniero de software autónomo de la empresa. Claude Fable 5 es el primero que se fiaría de dejar corriendo toda la noche.

El post tiene dos hilos. Uno es cómo decide Cognition que un modelo es mejor: no por una puntuación — "no nos fiamos de ninguna evaluación" — sino haciendo que sus desarrolladores con mejor criterio sometan cada modelo nuevo a un día real de trabajo, con el listón puesto en si el código es algo que de verdad se quedarían. El otro es qué cambió exactamente: el **horizonte**, es decir, cuánto tiempo se mantiene autosuficiente un agente antes de perder el hilo, y las tres conductas que sostuvieron una ejecución larga.

## ¿Cuándo es útil?
- Cuando decides si una tarea puede dejarse en manos de un agente durante horas sin supervisión.
- Cuando un agente termina una migración y no sabes si el resultado es de fiar.
- Cuando tus ingenieros han empezado a ignorar el triaje que produce un agente.
- Cuando un modelo arrasa en un benchmark y necesitas una forma de comprobarlo antes de creértelo.
- Cuando construyes un benchmark interno y decides qué debería premiar.
- Cuando discutís internamente si una nueva versión es realmente una mejora.

## Puntos clave
- **"No nos fiamos de ninguna evaluación."** Cognition ha visto modelos arrasar en un benchmark y desmoronarse en cuanto sus ingenieros los usaban: "nos hemos quemado así un montón de veces". Sus desarrolladores con mejor criterio someten cada modelo nuevo a un día real de trabajo; el listón es si el código es algo que se quedarían.
- **Frontier Code es un benchmark anti-slop.** Cognition lo construyó porque los existentes premiaban código que pasaba los tests pero no sobreviviría en un codebase real. En su subconjunto más difícil: modelo Opus previo ~10 %, Claude Fable 5 ~30 %.
- **Un salto merece sospecha.** Primera reacción: "¿Hay un bug? Esto no puede ser cierto." Normalmente los ingenieros discuten durante semanas; esta vez el dogfooding coincidió con los números. "Fue un poco impactante, la verdad."
- **El techo antiguo era el horizonte.** "Antes de Fable, podías delegar en agentes capaces de mantenerse en la tarea un par de minutos, quizá una hora." Después, las sesiones derivaban; cinco ideas a la vez hacían que los modelos anteriores se perdieran.
- **Terminar no es acertar.** En una migración de base de datos, un modelo Opus previo terminó técnicamente el trabajo pero introdujo por el camino una serie de bugs sutiles.
- **El triaje superficial destruyó la confianza.** Los modelos anteriores se quedaban en la superficie de los logs y estaban entrenados para responder pasara lo que pasara, así que "afirmaban con seguridad la primera cosa plausible que descubrían y ahí paraban". Los ingenieros aprendieron a ignorarlos.
- **Ocho horas, sin supervisión, con progreso real.** "Estaba a punto de irme a dormir y le dije: 'Vale, sigue trabajando en esto y no pares hasta que me despierte'. Y me despierto, y lleva ocho horas seguidas trabajando y haciendo progreso real."
- **Tres conductas sostuvieron el horizonte:** usar correctamente las herramientas internas de depuración de Cognition (recorrer logs en el navegador y concluir pese al ruido); enunciar las invariantes a las que se sujetaría antes de ejecutar una migración; y, en el triaje, identificar la causa raíz *y decir lo que no sabía*, que según Alberti es lo que reconstruye la confianza.
- **Un salto de escalón, más o menos anual.** El punto de referencia de Alberti es Claude 3.6 Sonnet a finales de 2024, el primer modelo capaz de encadenar herramientas de forma fiable y sostener una tarea de varios pasos; el uso interno se triplicó al meterlo en Devin.
- **Lo siguiente son las sesiones proactivas.** Devin ya puede vigilar un canal de Slack y meterse en un problema sin que le etiqueten, o monitorizar producción y triar un pico. Alberti espera que el 90 % de las sesiones de agente sean proactivas en uno o dos años.

## Recursos incluidos
- `skills/long-horizon-agent-runs/SKILL.md` — decide si la tarea tiene forma de horizonte, exige invariantes por adelantado, conecta las herramientas reales de depuración y pide un límite de confianza declarado.
- `skills/long-horizon-agent-runs/references/failure-modes.md` — las cinco formas en que fallan las ejecuciones largas, cada una junto a la conducta que la corrigió.
- `skills/long-horizon-agent-runs/templates/invariants-brief.md` — el brief en dos pasadas que hace que las invariantes se enuncien y se revisen antes de arrancar.
- `skills/long-horizon-agent-runs/examples/overnight-run.md` — la ejecución de ocho horas, la migración antes y después, y el triaje que gana confianza frente al que se ignora.
- `skills/dogfood-model-evaluation/SKILL.md` — haz del día de dogfooding la señal principal, elige evaluadores por criterio y trata la coincidencia entre puntuación y dogfooding como el resultado real.
- `skills/dogfood-model-evaluation/references/anti-slop-criteria.md` — lo que el post dice sobre Frontier Code, más los criterios implícitos en "¿sobreviviría en un codebase real?".
- `skills/dogfood-model-evaluation/templates/dogfood-day.md` — preparación, registro por tarea, veredicto binario y corroboración con tu benchmark.
- `guides/trusting-long-running-agents.{en,ko,es,ja}.md` — el relato completo en cuatro idiomas.

## Fuente
[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Blog de Claude, 10 de julio de 2026.
