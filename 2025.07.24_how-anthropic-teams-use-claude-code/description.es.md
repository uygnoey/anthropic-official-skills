[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Cómo los equipos de Anthropic usan Claude Code

## ¿De qué trata este post?
Este post comparte ejemplos concretos de cómo equipos de Anthropic usan Claude Code para navegar codebases, escribir pruebas, depurar, prototipar, documentar y automatizar flujos de trabajo.

## ¿Cuándo es útil?
- Al incorporarte a un codebase desconocido y necesitar entender dependencias rápidamente.
- Cuando quieres acelerar depuración, respuesta a incidentes, escritura de tests y prototipos rápidos.
- Cuando tienes flujos repetitivos (por ejemplo, analizar CSV grandes o generar muchas variantes de anuncios) que se benefician de automatización o subagentes especializados.

## Puntos clave
- Los equipos usan Claude Code para leer repositorios (incluyendo CLAUDE.md), encontrar archivos relevantes y explicar dependencias y pipelines de datos.
- Se usa para generar y refactorizar suites de tests completas, a veces integradas en bucles automáticos de feedback en PR.
- En incidentes, los equipos aportan stack traces y documentación para que Claude trace el flujo de control y proponga mitigaciones.
- Para desarrollo, usan bucles iterativos autónomos (escribir código → ejecutar tests → iterar) y explorar casos límite.
- Claude Code puede sintetizar múltiples fuentes en runbooks en Markdown.
- Algunos flujos usan varios subagentes especializados para generar grandes volúmenes de salidas con restricciones (p. ej., variantes de anuncios).
- El post también menciona un plugin de Figma para generar variantes de anuncios a partir de frames de diseño.

## Recursos incluidos
- Skill: **code-team-playbook** (patrones destilados del post).

## Fuente
- https://claude.com/blog/how-anthropic-teams-use-claude-code
