[English](./managed-agents-adoption.en.md) · [한국어](./managed-agents-adoption.ko.md) · **Español** · [日本語](./managed-agents-adoption.ja.md)

# Manual de adopción de Claude Managed Agents

Elaborado a partir del anuncio de lanzamiento del 8 de abril de 2026 de [Claude Managed Agents](https://claude.com/blog/claude-managed-agents). La publicación original es un anuncio de producto, por lo que esta guía reorganiza su contenido como un manual de toma de decisiones y adopción, sin incluir patrones de desarrollo reutilizables que el artículo no proporciona.

## Por qué un arnés gestionado

Antes de Managed Agents, lanzar un agente en producción exigía que el equipo de ingeniería construyera o integrara, como mínimo:

- Ejecución de código en sandbox
- Checkpointing para reanudar trabajos de larga duración
- Gestión de credenciales
- Permisos con alcance acotado sobre sistemas reales
- Trazabilidad de extremo a extremo
- Bucles de agente que debían reescribirse con cada actualización de modelo

Managed Agents combina un **arnés de orquestación** (que decide cuándo invocar herramientas, cómo gestionar el contexto y cómo recuperarse de errores) con esa infraestructura operacional, de modo que los equipos lancen el producto y no la plataforma.

## Qué incluye la suite

| Capacidad | Qué hace | Disponibilidad |
|---|---|---|
| Agentes de nivel productivo | Sandboxing seguro, autenticación y ejecución de herramientas gestionados por ti | Beta pública |
| Sesiones de larga duración | Operan de forma autónoma durante horas; el progreso y los resultados persisten ante desconexiones | Beta pública |
| Coordinación multiagente | Los agentes lanzan y dirigen a otros agentes para paralelizar trabajos complejos | Vista previa de investigación (solicitar acceso) |
| Gobernanza de confianza | Permisos con alcance acotado, gestión de identidades y trazabilidad de ejecución sobre sistemas reales | Beta pública |
| Modo basado en resultados | Defines los resultados y criterios de éxito; Claude se autoevalúa e itera | Vista previa de investigación (solicitar acceso) |
| Modo clásico de prompt y respuesta | Mayor control del flujo cuando lo necesitas | Beta pública |

## Lista de verificación: construir vs. adoptar

Revisa estos puntos antes de escribir cualquier runtime de agente propio. Cada uno corresponde a algo que Managed Agents ya gestiona.

- [ ] ¿Contamos con un equipo que se encargue del aislamiento en sandbox, el endurecimiento del kernel y la monitorización de escapes?
- [ ] ¿Estamos dispuestos a reconstruir nuestro bucle de agente en cada actualización de modelo de Claude?
- [ ] ¿Podemos mantener sesiones de larga duración de forma duradera ante desconexiones, despliegues y conmutaciones por error?
- [ ] ¿Disponemos de un mecanismo para rastrear cada llamada a herramienta, decisión y fallo de forma auditable?
- [ ] ¿Contamos con una infraestructura de permisos con alcance acotado que trate a los agentes como identidades de primera clase frente a sistemas reales?
- [ ] ¿Podemos entregar valor de producto en semanas, en lugar de meses, aunque primero construyamos todo lo anterior?

Cualquier respuesta negativa es un argumento a favor del runtime gestionado.

## Qué equipos lanzaron sobre Managed Agents

La publicación enumera las integraciones activas en el momento del lanzamiento. Úsalas como referencias de adopción, no como patrones prescriptivos:

| Equipo | Caso de uso | Fuente |
|---|---|---|
| Notion | Delegar trabajo a Claude dentro de un workspace de Notion; decenas de tareas en paralelo, el equipo colabora en los resultados | Eric Liu, PM — [artículo](https://claude.com/blog/claude-managed-agents) |
| Rakuten | Agentes empresariales para producto/ventas/marketing/finanzas integrados en Slack y Teams; cada especialista desplegado en una semana | Yusuke Kaji, GM of AI for Business — [artículo](https://claude.com/blog/claude-managed-agents) |
| Asana | AI Teammates — agentes colaborativos dentro de proyectos de Asana que asumen tareas y redactan entregables | Amritansh Raghav, CTO — [artículo](https://claude.com/blog/claude-managed-agents) |
| Vibecode | Plataforma de prompt a app desplegada; los clientes levantan infraestructura al menos 10 veces más rápido | Ansh Nanda, Co-founder — [artículo](https://claude.com/blog/claude-managed-agents) |
| Sentry | Seer (agente de depuración) combinado con un agente basado en Claude que escribe el parche y abre el PR | Indragie Karunaratne, Sr Director Eng AI/ML — [artículo](https://claude.com/blog/claude-managed-agents) |
| Atlassian | Agentes de desarrollo integrados en flujos de trabajo de Jira; tareas asignadas directamente desde Jira | Sanchan Saxena, SVP Teamwork Collection — [artículo](https://claude.com/blog/claude-managed-agents) |
| Casetext | Sistema que crea herramientas personalizadas sobre la marcha para responder cualquier consulta a partir de documentos y correspondencia de los usuarios | Javed Qadrud-Din, CTO — [artículo](https://claude.com/blog/claude-managed-agents) |
| Rewatch | Agente de preparación de reuniones con herramientas de calendario y contactos vía MCP; lanzado en días | John Han, Co-founder — [artículo](https://claude.com/blog/claude-managed-agents) |

## Ruta de adopción

Adopción paso a paso mapeada a las capacidades mencionadas en la publicación.

1. **Empieza por un ejecutor de tarea única.** El patrón común en la publicación es «agente especialista desplegado en una semana» — comienza ahí, no con la coordinación multiagente.
2. **Define tareas, herramientas y salvaguardas.** Esas son tus entradas; el arnés se encarga de la orquestación, la gestión del contexto y la recuperación ante errores.
3. **Ejecuta en Claude Platform.** Usa Claude Console, el nuevo CLI o Claude Code con el Skill integrado `claude-api` (`"start onboarding for managed agents in Claude API"`).
4. **Instrumenta e inspecciona.** Utiliza el trazado de sesiones, la analítica de integraciones y las herramientas de diagnóstico de Claude Console para revisar cada llamada a herramienta y cada modo de fallo.
5. **Decide si usar el modo basado en resultados.** Si tu tarea tiene criterios de éxito verificables, solicita acceso a la vista previa de investigación del modo de resultados; de lo contrario, mantén el modo de prompt y respuesta.
6. **Añade coordinación multiagente solo cuando sea necesario.** Solicita acceso a la vista previa de investigación cuando los agentes especialistas en paralelo aporten un valor medible.

## Modelo de precios a tener en cuenta

- Tarifas estándar de tokens de Claude Platform
- Más **$0.08 por hora de sesión** de runtime activo

Dos variables de coste a planificar: el consumo de tokens por decisión y el tiempo real que un agente permanece activo. Las sesiones autónomas de larga duración generan más costes de horas de sesión que las ejecuciones cortas e intensivas; ten en cuenta ese equilibrio en la planificación de capacidad.

## Lo que esta publicación **no es**

- No es una referencia sobre cómo construir tu propio arnés de agente
- No define roles de agente con nombre ni reglas operacionales
- No prescribe hooks, estilos de salida ni empaquetado de plugins

Trata la publicación como una referencia de adopción y alcance. Para patrones reutilizables de Claude Code, consulta los Skills y Subagents del resto de este repositorio.

## Fuente

[Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) (publicado el 2026-04-08).
