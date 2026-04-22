[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Crear agentes con Skills: equipar agentes para trabajo especializado

## ¿De qué trata este post?
Este post explica qué son las Agent Skills, cómo empaquetan conocimiento de dominio para agentes y por qué la divulgación progresiva (metadatos → SKILL.md → references) permite escalar a muchas skills.

## ¿Cuándo es útil?
- Cuando quieres que los agentes apliquen reglas/estándares/workflows de dominio sin tener que reexplicarlos en cada conversación.
- Cuando necesitas muchas skills pero debes mantener el uso de contexto bajo control.

## Puntos clave
- Primero se muestra el frontmatter YAML (name + description); el SKILL.md completo y los archivos de referencia se cargan solo cuando se necesitan.
- El post enfatiza una estructura de tres niveles: metadatos (~50 tokens), SKILL.md (~500 tokens) y archivos de referencia (2.000+ tokens) bajo demanda.
- Las skills pueden incluir archivos de apoyo (p. ej., docs, guías para slides y scripts) y referenciarlos desde el SKILL.md.

## Recursos incluidos
- Skill: `skills-packaging-principles` (guía de estructura + plantillas)
- Guide: `skills-packaging-guide` (resumen y layout recomendado)

## Fuente
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
