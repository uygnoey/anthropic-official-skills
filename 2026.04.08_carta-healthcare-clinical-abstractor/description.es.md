[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo Carta Healthcare logra que la IA razone como un abstractor clínico

## ¿De qué trata este post?
Este post explica cómo Carta Healthcare construyó Lighthouse, una plataforma de abstracción de datos clínicos que usa Claude para razonar sobre historiales médicos y alcanzar alta precisión a escala.

## ¿Cuándo es útil?
Es útil si estás construyendo un sistema de IA que debe tomar decisiones justificables y acotadas en el tiempo a partir de documentos de dominio desordenados (especialmente cuando las personas deben revisar y confiar en los resultados).

## Puntos clave
- La ingeniería de contexto importa tanto como el modelo: decide qué evidencia incluir/excluir y en qué orden, y ensambla el contexto específico del paciente en tiempo de ejecución.
- Usa anclas temporales explícitas (p. ej., la hora de inicio del procedimiento) al pedir valores “pre‑procedimiento” para que el modelo aplique la lógica temporal correcta.
- Construye temprano un marco de evaluación y hazlo lo bastante granular para aislar si los fallos vienen del prompt, del contexto faltante o de brechas de recuperación.
- Cierra el ciclo con expertos del dominio: incorpora rápidamente el feedback de los abstractores en actualizaciones de prompts/contexto.
- Prioriza la transparencia: muestra la evidencia y el razonamiento del modelo para que los abstractores puedan validar.

## Recursos incluidos
- Una skill de Claude Code para “ingeniería de contexto para extracción acotada en el tiempo”, con plantillas reutilizables y checklist de evaluación.

## Fuente
- https://claude.com/blog/carta-healthcare-clinical-abstractor
