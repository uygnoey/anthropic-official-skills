[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta dos capacidades para agentes de larga duración en la Claude Developer Platform: la edición de contexto (elimina automáticamente resultados obsoletos de herramientas cuando se acerca el límite de tokens) y la herramienta de memoria (persiste información fuera de la ventana de contexto en un almacén basado en archivos controlado por el desarrollador).

## ¿Cuándo es útil?
Es útil al construir agentes que ejecutan muchos pasos o funcionan a través de varias sesiones, cuando quieres evitar el agotamiento del contexto pero conservar decisiones, hallazgos y estado clave entre turnos.

## Puntos clave
- La edición de contexto elimina llamadas/resultados obsoletos cerca del límite de tokens manteniendo el flujo de la conversación.
- La herramienta de memoria guarda información en un directorio dedicado gestionado por el desarrollador (del lado del cliente mediante llamadas a herramientas).
- El post describe que Claude Sonnet 4.5 mejora la conciencia de contexto para estos flujos.

## Recursos incluidos
- Skill: una guía práctica para decidir qué debe quedarse en contexto y qué debe escribirse en memoria persistente, más una lista de verificación de decisiones comunes de “guardar vs mantener”.

## Fuente
- https://claude.com/blog/context-management
