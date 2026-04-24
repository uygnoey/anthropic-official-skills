[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Crear layouts web responsivos

## ¿De qué trata este post?
Este post explica cómo usar Claude (especialmente Claude Code) para generar y refactorizar layouts responsivos que funcionen bien en una amplia gama de tamaños de viewport.

## ¿Cuándo es útil?
- Cuando anchos fijos y reglas rígidas provocan desbordes u otros fallos de layout en tablets y móviles.
- Cuando quieres pasar de iterar manualmente con breakpoints a refactors más sistemáticos y validados con pruebas.

## Puntos clave
- Claude Code puede leer tus hojas de estilo, detectar restricciones rígidas y reemplazarlas por alternativas flexibles (p. ej., `max-width`, `flex-basis`, patrones de grid con `auto-fit`).
- Añade media queries específicas por breakpoint y valida en viewports pequeños (p. ej., 320px, 512px) para evitar overflow horizontal.
- Genera pruebas con Playwright para validar el comportamiento responsivo en tamaños de dispositivos comunes.

## Recursos incluidos
- Skill: `responsive-layout-refactor` (instrucciones, prompts de ejemplo, snippets)

## Fuente
- https://claude.com/blog/build-responsive-web-layouts
