[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?

Este post es una guía práctica para escribir Skills para Claude: qué hace que una Skill se active de forma fiable, cómo estructurar SKILL.md y cómo probar e iterar.

## ¿Cuándo es útil?

Es útil cuando quieres crear una Skill reutilizable (en Claude apps, Claude Code o la Skills API) y necesitas orientación sobre nombres, descripciones (activación), estructura de instrucciones, pruebas y control del tamaño de contexto.

## Puntos clave

- Una Skill tiene tres componentes principales: name, description (clave para la activación) e instructions.
- La description debe ser específica: qué hace, cuándo debe activarse y para qué no debe usarse.
- Mantén SKILL.md escaneable con fases claras, prerrequisitos, manejo de errores y ejemplos.
- Usa archivos complementarios para no inflar el contexto (enfoque de “menú” con enlaces a archivos adicionales).
- Prueba con una matriz: casos normales, casos límite y peticiones fuera de alcance; itera según el uso real.

## Recursos incluidos

- Plantilla adaptable para redactar Skills: `skills/skill-authoring-guide/templates/skill-template.md`
- Plantilla de matriz de pruebas para validación: `skills/skill-authoring-guide/templates/test-matrix.md`
- Extractos derivados de los ejemplos de SKILL.md del post: `skills/skill-authoring-guide/examples/skill-examples.md`

## Fuente

- https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
