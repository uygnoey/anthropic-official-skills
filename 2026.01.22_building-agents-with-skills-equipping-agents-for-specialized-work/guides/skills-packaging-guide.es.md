[English](./skills-packaging-guide.en.md) · [한국어](./skills-packaging-guide.ko.md) · **Español** · [日本語](./skills-packaging-guide.ja.md)

# Guía para empaquetar Skills

## Resumen
Esta guía resume el enfoque recomendado en el post para estructurar Agent Skills mediante divulgación progresiva.

## Estructura recomendada
- Mantén el frontmatter YAML mínimo (name + description).
- Pon instrucciones accionables en `SKILL.md`.
- Mueve material extenso a `references/` y enlázalo desde `SKILL.md`.

## Por qué ayuda
La divulgación progresiva mantiene utilizable una biblioteca grande de skills: el modelo puede ver muchos “títulos” con poco costo y solo cargar el detalle cuando hace falta.

## Fuente
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
