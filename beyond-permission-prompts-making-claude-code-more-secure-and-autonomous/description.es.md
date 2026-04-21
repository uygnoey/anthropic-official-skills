[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta dos funciones nuevas de Claude Code basadas en el **sandboxing nativo** para que la programación con agentes sea más segura y más autónoma: un bash en sandbox (vista previa de investigación) y Claude Code en la web (sandbox en la nube).

## ¿Cuándo es útil?
Es útil cuando quieres que Claude Code (u otro agente de programación) pueda ejecutar más acciones sin pedir permisos de forma constante, reduciendo a la vez el riesgo de inyección de prompts y otros usos no deseados de herramientas.

## Puntos clave
- El enfoque base de Claude Code es por permisos (solo lectura por defecto), pero las aprobaciones frecuentes pueden causar “fatiga de aprobación”.
- El post sostiene que el sandboxing puede ser más seguro y más autónomo que pedir permisos acción por acción.
- Un sandboxing efectivo requiere **aislamiento del sistema de archivos** (limitar directorios y escrituras) y **aislamiento de red** (limitar hosts a los que se puede conectar).
- El bash en sandbox aplica restricciones con primitivas del sistema operativo (p. ej., bubblewrap en Linux y seatbelt en macOS).
- Claude Code en la web ejecuta cada sesión en un sandbox aislado en la nube y mantiene credenciales sensibles fuera del sandbox, usando un proxy para operaciones de git.

## Recursos incluidos
- El post no incluye archivos de políticas, configuraciones de hooks ni scripts listos para usar; se centra en conceptos y funciones del producto.

## Fuente
- https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
