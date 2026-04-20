[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Personalizar Claude Code con CLAUDE.md

## ¿Qué es esta habilidad?
Elimina la necesidad de explicarle a Claude Code la estructura del proyecto, el estilo de código y los comandos habituales en cada sesión. Un archivo `CLAUDE.md` en la raíz del proyecto se **carga automáticamente en el prompt de sistema de Claude al inicio de cada conversación**.

## Cuándo usar
- Un equipo quiere un comportamiento consistente de Claude en un repositorio compartido (commitear el archivo)
- Un monorepo donde los subproyectos comparten reglas (colocarlo en el directorio padre)
- Preferencias globales personales (`~/CLAUDE.md`)
- Cuando te das cuenta de que repites las mismas instrucciones en cada sesión

## Principios fundamentales
1. **Empieza con `/init`** — deja que Claude analice el código base y elabore el borrador.
2. **Organiza en torno a tres ejes**: (1) mapa del proyecto, (2) conexiones de herramientas, (3) flujos de trabajo estándar.
3. **Captura solo problemas reales.** Omite las preocupaciones teóricas.
4. **Sin secretos.** Nunca incluyas claves API, credenciales ni detalles de vulnerabilidades.

## Secciones recomendadas
| Sección | Propósito | Contenido |
|---|---|---|
| Project map | Visión general del proyecto | Descripción en una línea, árbol de directorios, dependencias clave, patrones de arquitectura |
| Tool connections | Comandos personalizados / MCP | Cómo invocar comandos personalizados, reglas para servidores MCP |
| Workflows | Procedimientos estándar | Preguntas previas al trabajo, explore→plan→code→commit, reglas de TDD |

## Ejemplo: proyecto FastAPI

```markdown
# Project Context

When working with this codebase, prioritize readability over cleverness.
Ask clarifying questions before making architectural changes.

## About This Project

FastAPI REST API for user authentication and profiles.
Uses SQLAlchemy for database operations and Pydantic for validation.

## Key Directories

- `app/models/` - database models
- `app/api/` - route handlers
- `app/core/` - configuration and utilities

## Standards

- Type hints required on all functions
- pytest for testing (fixtures in `tests/conftest.py`)
- PEP 8 with 100 character lines

## Common Commands

​```bash
uvicorn app.main:app --reload  # dev server
pytest tests/ -v               # run tests
​```

## Notes

All routes use `/api/v1` prefix. JWT tokens expire after 24 hours.
```

## Ejemplo: reglas de uso de herramienta MCP (Slack)

```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

## Lista de comprobación para la autoría
- [ ] Iniciado desde `/init`
- [ ] El mapa de directorios coincide con la realidad
- [ ] Comandos bash habituales listados
- [ ] Cero secretos / credenciales
- [ ] Flujos de trabajo del equipo (pruebas, PRs) recogidos
- [ ] Ninguna regla sin un problema real y recurrente que la justifique

## Consejos de mantenimiento
- En el chat, pulsa la tecla de las comillas inversas triples para añadir directamente una instrucción repetida a CLAUDE.md.
- Convierte los flujos de trabajo repetitivos en comandos slash personalizados bajo `.claude/commands/` (archivos MD, usa `$ARGUMENTS` / `$1`).
- Usa `/clear` para reiniciar el contexto; delega tareas aisladas a subagentes.
- Divide las guías muy largas en archivos `.md` separados y referencíalos desde CLAUDE.md.

## Fuente
Basado en [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) (publicado el 2025-11-25). Para una orientación autorizada, consulta siempre el original.
