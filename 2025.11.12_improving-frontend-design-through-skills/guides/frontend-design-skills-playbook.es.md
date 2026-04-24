[English](./frontend-design-skills-playbook.en.md) · [한국어](./frontend-design-skills-playbook.ko.md) · **Español** · [日本語](./frontend-design-skills-playbook.ja.md)

# Diseño frontend a través de Skills: un manual práctico

Esta guía resume los patrones concretos de prompting y reutilización descritos en el artículo fuente, orientados a convertirlos en una Skill reutilizable que puedas cargar bajo demanda.

## El problema: "convergencia distribucional" en el output de UI con IA
El artículo describe cómo las generaciones de UI a menudo convergen en un aspecto genérico (familias tipográficas comunes y gradientes predecibles), lo que puede diluir la identidad de marca.

## El enfoque: mantener las directrices de diseño reutilizables con Skills
- Almacena las directrices de diseño como un archivo de Skill (generalmente markdown) para que Claude las cargue solo cuando la tarea lo requiera.
- Esto evita la sobrecarga permanente de contexto en tu configuración de prompt predeterminada.

## Proporciona directrices en la "altitud correcta"
- Demasiado abstracto: las peticiones estéticas vagas no cambian los resultados de forma fiable.
- Demasiado concreto: las prescripciones excesivamente específicas y rígidas (por ejemplo, códigos hex fijos y microgestión pixel a pixel) pueden reducir la flexibilidad.
- Mejor: especifica una dirección coherente (tipografía, referencias de tema, movimiento, tratamiento del fondo) con margen para la implementación.

## Áreas de orientación concretas del artículo
### Tipografía
- Evita las fuentes predeterminadas (el artículo nombra explícitamente las fuentes comunes que hay que evitar).
- Elige familias tipográficas y combinaciones más distintivas.
- Usa el contraste: pesos extremos y saltos de escala notables.

### Temas
El artículo proporciona un ejemplo temático de RPG:
- Paletas de inspiración fantástica
- Bordes ornamentados
- Texturas tipo pergamino
- Iluminación dramática
- Tipografía serif medieval

### Movimiento
- Usa animaciones CSS y revelaciones escalonadas cuando sea apropiado.
- Para React, utiliza una librería de movimiento cuando sea útil.

### Fondos
- Usa gradientes y patrones intencionalmente para reforzar el tema.
- Prefiere patrones geométricos o tratamientos con textura frente a los valores predeterminados predecibles.

## Nota sobre la generación de artefactos (del artículo)
El artículo menciona el uso de una skill adicional para crear artefactos web más ricos con herramientas modernas (por ejemplo, React + Tailwind y librerías de componentes), empaquetados en un único artefacto HTML.

## Fuente
Elaborado a partir de [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) (publicado el 2025-11-12).
