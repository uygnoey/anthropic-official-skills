[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## ¿De qué trata este post?
Presenta el modo Auto en Claude Code: un modo de permisos en el que Claude puede aprobar automáticamente muchas acciones de herramientas, con salvaguardas que bloquean comportamientos riesgosos.

## ¿Cuándo es útil?
Es útil cuando quieres ejecutar tareas largas con menos interrupciones por aprobaciones, pero no quieres omitir por completo los permisos con --dangerously-skip-permissions.

## Puntos clave
- Los permisos predeterminados de Claude Code piden aprobación en cada escritura de archivo y comando bash; el modo Auto busca reducir esas interrupciones.
- Antes de cada llamada a herramienta, un clasificador revisa acciones potencialmente destructivas (p. ej., borrado masivo, exfiltración de datos sensibles, ejecución de código malicioso).
- Las acciones consideradas seguras se ejecutan automáticamente; las riesgosas se bloquean y Claude debe intentar otro enfoque, con una solicitud al usuario como respaldo si se bloquea repetidamente.
- Reduce el riesgo frente a omitir permisos, pero no lo elimina; se sigue recomendando usarlo en entornos aislados.
- Los desarrolladores pueden habilitarlo con `claude --enable-auto-mode` (y alternar con Shift+Tab); los administradores pueden deshabilitarlo con el ajuste administrado `disableAutoMode`.

## Recursos incluidos
- 1 skill (auto-mode-permissions)

## Fuente
- Auto mode for Claude Code (2026-03-24): https://claude.com/blog/auto-mode
