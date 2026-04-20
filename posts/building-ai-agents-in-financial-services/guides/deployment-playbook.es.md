[English](./deployment-playbook.en.md) · [한국어](./deployment-playbook.ko.md) · **Español** · [日本語](./deployment-playbook.ja.md)

# Manual de despliegue: agentes de IA en servicios financieros

Referencia detallada elaborada a partir de [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) (blog de Claude, publicado el 2025-10-30). Carga este archivo solo cuando el usuario solicite orientación más profunda que la que proporciona SKILL.md — por ejemplo, arquitectura de integración, planificación de despliegue por fases, diseño de controles de riesgo o ejemplos concretos del sector.

## Despliegue por fases

### Fase 1 — Encontrar el punto de partida
Elige objetivos de alto impacto y bajo riesgo donde la supervisión humana ya exista o donde las consecuencias de una automatización imperfecta sigan siendo mínimas. Buenos candidatos:
- Triaje de atención al cliente
- Recuperación de conocimiento interno
- Validación rutinaria de datos
- Detección de patrones de transacciones inusuales
- Supervisión de plazos de cumplimiento
- Clasificación automatizada de documentos

Empieza con una tarea sencilla y bien definida. Establece métricas claras antes de ampliar el alcance.

### Fase 2 — Escalar en toda la organización
Construye bases reutilizables en lugar de soluciones puntuales. Una única capacidad de procesamiento de documentos puede servir para:
- Conciliaciones bancarias y procesamiento de facturas
- Equipos de cumplimiento que analizan documentos regulatorios
- Extracción de datos financieros entre departamentos

Gánate la confianza (a) siendo transparente con los clientes sobre la interacción con IA frente a humanos, (b) capacitando al personal para entender cómo funcionan los agentes y cuándo escalar, y (c) presentando los agentes como una mejora, no como un reemplazo.

### Fase 3 — Avanzar hacia casos de uso complejos
Solo una vez que la base sea estable. Requisitos:
- Registros de auditoría completos que rastreen cada decisión del agente y las fuentes de datos utilizadas
- Sistemas de monitoreo en tiempo real que detecten casos extremos
- Protocolos de escalado que deriven los casos complejos a los especialistas adecuados
- Métricas de rendimiento que midan los resultados de negocio y el éxito de la integración en el flujo de trabajo — no solo la precisión técnica

## Integración y arquitectura

### Desafíos de la infraestructura heredada
- Incompatibilidades entre plataformas de banca central de distintos proveedores
- Silos de datos por departamento que requieren orquestación entre sistemas
- Dificultades de integración con mainframes heredados
- Necesidades de sincronización en tiempo real

### Enfoques de integración
1. **Integración directa** cuando la plataforma del agente soporta el sistema destino de forma nativa.
2. **Conectores personalizados** mediante APIs o enfoques MCP.
3. **Sistemas de middleware** para cubrir brechas manteniendo la integridad de las transacciones y los registros de auditoría.

### Flujo de datos agentico
Los agentes ingieren información de múltiples fuentes no relacionadas y procesan tipos de datos heterogéneos: registros de transacciones, datos de mercado, documentos regulatorios. Patrón de ejemplo de la fuente: en lugar de que un analista extraiga datos manualmente de cinco sistemas distintos, un agente monitorea los patrones de transacciones en esos sistemas y presenta una recomendación fundamentada.

### Bases reutilizables
Construye infraestructura compartida que sirva a múltiples departamentos. Prioriza sistemas modulares que puedan evolucionar con el avance de las capacidades de IA.

## Controles de riesgo

La implementación de riesgo en tiempo real debe incluir:
- **Razonamiento transparente** que los profesionales financieros puedan validar y explicar a los clientes
- **Vías de escalado claras** para situaciones complejas o ambiguas
- **Capacidades de anulación** que permitan a los asesores rechazar las recomendaciones de IA cuando las circunstancias del cliente lo justifiquen
- **Valores predeterminados de seguridad** que prioricen la protección del cliente sobre la eficiencia operativa
- **Autorización con humano en el bucle** para acciones de alto riesgo
- **Estado seguro conocido** ante fallos

Mantén el juicio humano firmemente en el bucle durante los primeros despliegues. Informa a los clientes sobre las interacciones con IA.

## Regulación y cumplimiento

Los agentes deben saber qué marcos regulatorios se aplican a cada decisión y cómo documentar las acciones para los distintos requisitos de auditoría. Organismos relevantes mencionados: SEC, FDIC, autoridades bancarias estatales y organismos internacionales.

Preocupaciones específicas de cumplimiento:
- Cumplimiento de SOC 2 y PCI DSS para los flujos de trabajo de procesamiento de datos con IA
- Validación basada en evidencia de la precisión en la evaluación de riesgos
- Requisitos de documentación para los registros de auditoría de decisiones de IA
- Incorporar observabilidad y trazabilidad en las soluciones agenticas desde el primer día

## Ejemplos documentados

| Organización | Caso de uso | Resultado reportado |
|---|---|---|
| Investigación McKinsey | Agentes de IA en detección de fraude | Ganancias de productividad del 200–2000%; un miembro del equipo puede supervisar más de 20 agentes en flujos de trabajo de detección de delitos financieros |
| Norges Bank Investment Management (NBIM) | Tareas analíticas y operativas | Los empleados ahorran cientos de horas acumuladas por semana |
| Intuit TurboTax | Asistente financiero de IA para explicaciones fiscales | Valoraciones de clientes más altas que las experiencias no basadas en Claude en la temporada fiscal anterior |
| Brex | Detección de anomalías | Revisa el 100% de las transacciones; agrupa proactivamente gastos relacionados, señala preocupaciones de política, proporciona explicaciones y acciones recomendadas |
| Block | Agente de IA interno | 4.000 usuarios activos de 10.000 empleados en 15 perfiles de trabajo; la adopción se duplicó en un mes; crecimiento del 40-50% en el uso semanal |
| Campfire | Asistencia a equipos internos | Prototipos de diseño, cierre de casos de operaciones, consultas de contabilidad |
| Verisk | Agentes a escala mediante Claude en AWS Bedrock | Mencionado como ejemplo de escala |
| Visa, Citi, NBIM | Transformación del sector | Mencionados en la sección "Learn more" |

Patrones generales de cara al consumidor mencionados: detección de posibles cargos por descubierto, sugerencia de estrategias de ahorro, asistentes virtuales multilingües que gestionan cientos de millones de interacciones anuales, agentes de servicio al cliente que automatizan consultas de saldo y sustitución de tarjetas, monitoreo en tiempo real de millones de transacciones.

## Lista de verificación para la toma de decisiones

Antes de aprobar un despliegue:
- [ ] ¿Existe ya supervisión humana para este flujo de trabajo?
- [ ] ¿Son aceptables las consecuencias de una automatización imperfecta?
- [ ] ¿Están definidas métricas de éxito claras?
- [ ] ¿Tiene el agente integración directa con los sistemas necesarios? En caso negativo, ¿está presupuestada una vía de conector/middleware?
- [ ] ¿Están identificados los marcos regulatorios aplicables por tipo de decisión?
- [ ] ¿Están resueltas las preocupaciones de SOC 2 / PCI DSS en el procesamiento de datos?
- [ ] ¿Se captura un registro de auditoría de cada decisión y fuente de datos?
- [ ] ¿Están diseñados el razonamiento transparente, el escalado, la anulación y los valores predeterminados de seguridad?
- [ ] ¿Existe un punto de autorización humana en el bucle para acciones de alto riesgo?
- [ ] Para uso orientado al cliente: ¿se informa de la interacción con IA y existe una vía de acceso a un humano?

## Fuente
Elaborado a partir de [Building AI agents for financial services | Claude](https://claude.com/blog/building-ai-agents-in-financial-services) (publicado el 2025-10-30). Consulta el original para obtener orientación autoritativa.
