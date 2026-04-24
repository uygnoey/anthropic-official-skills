[English](./three-patterns-app-harness.en.md) · [한국어](./three-patterns-app-harness.ko.md) · **Español** · [日本語](./three-patterns-app-harness.ja.md)

# Tres patrones para construir aplicaciones que evolucionen al ritmo de Claude

Esta guía resume tres patrones del artículo fuente para diseñar aplicaciones (incluidos los agentes) que se mantengan al día con las capacidades cambiantes de Claude mientras equilibran la latencia y el costo.

## Patrón 1 — Usa lo que Claude ya conoce
- Prioriza construir con herramientas que Claude ya entiende bien.
- El artículo destaca el uso de una **herramienta bash** y una **herramienta de editor de texto** para visualizar/crear/editar archivos como una base sólida.
- Las construcciones de nivel superior (por ejemplo, skills, llamadas programáticas a herramientas, memoria) pueden construirse sobre estas herramientas generales.

## Patrón 2 — Pregúntate "¿qué puedo dejar de hacer?" (revisa los supuestos del arnés)
Los arneses de agente a menudo incluyen estructura que codifica supuestos sobre lo que Claude no puede hacer. A medida que Claude mejora, esos supuestos pueden convertirse en peso muerto.

### Deja que Claude orqueste sus propias acciones
- Evita forzar cada resultado de herramienta a la ventana de contexto de Claude.
- Si Claude solo necesita una porción de la salida (por ejemplo, una columna de una tabla grande), introducir todas las filas en el contexto es lento y costoso.
- En su lugar, proporciona a Claude una herramienta de ejecución de código (bash o un REPL) para que pueda escribir código que:
  - llame a herramientas,
  - filtre/agregue la salida,
  - y canalice los resultados hacia la siguiente acción,
  devolviendo solo la salida final mínima al contexto.

### Deja que Claude gestione su propio contexto
- Evita sobrecargar los prompts del sistema con instrucciones específicas de la tarea que rara vez se aplican.
- Usa divulgación progresiva:
  - se precarga un resumen breve (por ejemplo, el frontmatter YAML de una skill),
  - y Claude lee el contenido completo solo cuando es necesario.
- Elimina el contexto obsoleto o irrelevante mediante la edición selectiva de contexto.
- Usa subagentes para dividir el trabajo en ventanas de contexto nuevas cuando aislar una tarea sea beneficioso.

### Deja que Claude persista su propio contexto
- Los agentes de larga duración pueden superar una sola ventana de contexto.
- Usa compactación para resumir el contexto pasado manteniendo la continuidad.
- Usa una carpeta de memoria para que Claude pueda escribir información importante en archivos y leerla más tarde.
- El ejemplo del juego del artículo contrasta las notas tipo transcripción frente a los aprendizajes tácticos y destilados organizados en un directorio.

## Patrón 3 — Establece límites con cuidado
Los arneses de agente deben imponer límites de UX, costo y seguridad.

### Diseña el contexto para maximizar los aciertos de caché
Dado que la API de Messages es sin estado, el arnés reenvía el contexto anterior en cada turno. El artículo proporciona principios para aumentar la reutilización de la caché de prompts:
- **Static first, dynamic last**: coloca el contenido estable (prompt del sistema, herramientas) antes que las entradas que cambian con frecuencia.
- **Messages for updates**: añade actualizaciones (por ejemplo, un bloque `system-reminder`) en lugar de editar el texto del prompt anterior.
- **Don't change models**: las cachés son específicas del modelo; cambiar de modelo las invalida (usa un subagente si necesitas un modelo más económico).
- **Carefully manage tools**: agregar/eliminar herramientas invalida las cachés; usa tool search para el descubrimiento dinámico sin romper la caché.
- **Update breakpoints**: para aplicaciones con múltiples turnos, avanza el punto de corte para que la caché refleje el prefijo estable más reciente; usa auto-caching.

### Usa herramientas declarativas para UX, observabilidad y seguridad
- Una herramienta bash otorga amplio poder, pero el arnés solo ve una cadena de comandos sin tipo.
- Promover acciones a herramientas tipadas y declarativas le da al arnés puntos de enganche para:
  - interceptar y controlar acciones (por ejemplo, confirmación del usuario para llamadas a API externas),
  - añadir verificaciones de seguridad (por ejemplo, verificaciones de obsolescencia para herramientas de edición),
  - renderizar elementos de UX (modales, opciones, bloqueo para la entrada del usuario),
  - y registrar/trazar/reproducir argumentos estructurados para la observabilidad.
- Reevalúa periódicamente qué acciones merecen ser promovidas; el artículo describe el modo automático de Claude Code usando un segundo Claude para juzgar la seguridad de bash como un posible patrón de límite.

## Práctica continua
- Vuelve a probar los supuestos siempre que cambien las capacidades de Claude.
- Elimina los reinicios o el scaffolding que existían solo para compensar las limitaciones de modelos anteriores.

## Fuente
Elaborado a partir de [Harnessing Claude's Intelligence: 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) (publicado el 2026-04-02).
