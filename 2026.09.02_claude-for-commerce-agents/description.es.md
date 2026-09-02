[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

# Construir agentes de comercio con Claude

## ¿De qué trata este post?

Un anuncio de producto. Anthropic publicó un blueprint abierto para construir agentes de
comercio, con implementaciones de referencia de un **agente de compras** y un **agente de
comerciante**, además de ejemplos de retail, viajes, telecomunicaciones y ticketing. El dato
destacado: los minoristas que operan agentes de compras sobre Claude han visto carritos hasta un
35% más grandes y compradores un 60% más propensos a completar la compra.

El agente de compras se integra en una aplicación o sitio web y cubre búsqueda en catálogo,
armado de pedidos multi-artículo, preferencias, comparación de productos, construcción del
carrito para el traspaso al checkout, y preguntas de atención al cliente. El agente de
comerciante responde preguntas de rendimiento de ventas, sigue el inventario, recomienda precios
y promociones y redacta campañas — siempre como sugerencias que una persona aprueba antes del
despliegue.

Shopify, Priceline, Wix, Zomato, Fetch y Square figuran como constructores sobre él, con
Accenture, Mastercard y Visa como socios.

## ¿Cuándo es útil?

- Empiezas un proyecto de agente de comercio y quieres una referencia funcionando en lugar de un
  repositorio en blanco.
- Necesitas acotar cuáles de tus sistemas existentes — catálogo, carrito, checkout, preferencias,
  historial de pedidos — tendrá que llamar el agente.
- Estás decidiendo si construir primero el lado del comprador o el del vendedor.
- Necesitas saber dónde puede correr el despliegue: Claude API, Amazon Bedrock, Microsoft
  Foundry o Google Cloud Vertex AI.

## Puntos clave

- **Dos agentes de referencia, un blueprint.** Compras (orientado al consumidor) y comerciante
  (orientado al negocio), en
  [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents).
- **Los puntos de integración del agente de compras** son búsqueda en catálogo, gestión del
  carrito, checkout, preferencias del cliente e historial de pedidos. El agente llama a sistemas
  que ya operas.
- **Los guardarraíles de compras vienen incluidos:** precios y productos limitados a los datos
  del catálogo, y nada de patrones manipuladores de upsell.
- **El principio del comerciante:** los agentes sugieren cambios; las personas aprueban antes del
  despliegue.
- **Despliega donde corre Claude** — Claude API, Amazon Bedrock, Microsoft Foundry, Google Cloud
  Vertex AI.
- **La puesta en marcha se reporta rápida.** Los ingenieros de Wix tuvieron agentes de comercio
  funcionando en quince minutos; Fetch puso ambos agentes en local en menos de una hora, con
  conversaciones en vivo funcionando al primer intento.
- **La confianza es la restricción declarada.** Ambos socios de pagos lo plantean igual — Visa:
  *"La IA transformará radicalmente el comercio, pero la confianza debe seguir en el centro de
  cada transacción."*
- **El detalle de ingeniería es otro post.** Arquitectura, latencia, caché, memoria, seguridad y
  evals están en la guía complementaria, *Una guía sobre la anatomía de los agentes de comercio
  eficaces*.

## Recursos incluidos

- `agents/shopping-agent.md` — el agente orientado al consumidor: puntos de integración,
  capacidades y los guardarraíles de anclaje al catálogo y de no-upsell-manipulador.
- `agents/merchant-agent.md` — el agente orientado al negocio: capacidades y el principio de
  sugerir sin aplicar.
- `skills/commerce-agent-blueprint/SKILL.md` — cómo acotar y levantar un despliegue desde el
  blueprint.
- `skills/commerce-agent-blueprint/references/blueprint-contents.md` — qué trae el repositorio,
  capacidad por capacidad.
- `skills/commerce-agent-blueprint/references/deployment-options.md` — dónde corre, el ecosistema
  de socios y quién está construyendo sobre él.

## Fuente

- https://claude.com/blog/claude-for-commerce-agents (publicado 2026-09-02)
- Análisis técnico: https://claude.com/blog/the-anatomy-of-effective-commerce-agents
