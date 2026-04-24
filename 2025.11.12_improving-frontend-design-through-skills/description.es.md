[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Mejorar el diseño frontend mediante Skills

## ¿De qué trata este post?
Este post explica cómo usar las **Skills** de Claude como guías de diseño reutilizables y bajo demanda, para que las generaciones de frontend/UI no converjan en los "valores por defecto de la IA" más genéricos (por ejemplo, fuentes comunes y gradientes predecibles).

## ¿Cuándo es útil?
- Cuando necesitas una UI con identidad de marca para experiencias orientadas al cliente (páginas de aterrizaje, dashboards, aplicaciones) en lugar de maquetaciones genéricas.
- Cuando quieres mantener las reglas de diseño reutilizables sin inflar permanentemente tus prompts base.
- Cuando generas artefactos web que se benefician de stacks modernos (React + Tailwind + librerías de componentes) en lugar de ejemplos simples en un solo archivo.

## Puntos clave
- Las Skills se guardan como archivos que Claude puede cargar solo cuando es necesario, permitiéndote mantener las restricciones de diseño especializadas separadas del prompting general.
- Proporciona orientación a la "altitud adecuada": evita directrices demasiado vagas, pero también evita el micromanagement frágil de píxeles y valores hex.
- Aleja las elecciones de tipografía, tema, movimiento y fondo de los valores por defecto comunes ofreciendo alternativas concretas.
- El post incluye bloques de prompt para elecciones tipográficas, un tema RPG y un bloque `frontend_aesthetics` más completo.

## Recursos incluidos
- Skill: `skills/frontend-design-aesthetics/SKILL.md`
- Guide (en/ko): `guides/frontend-design-skills-playbook.*.md`

## Fuente
Basado en la publicación oficial del blog de Claude: https://claude.com/blog/improving-frontend-design-through-skills (publicado el 2025-11-12).
