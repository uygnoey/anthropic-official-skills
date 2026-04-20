[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Mejores prácticas de prompt engineering para Claude

## Qué es esta habilidad
Una referencia rápida extraída de la guía oficial de Anthropic sobre prompt engineering. Incluye cinco técnicas fundamentales (claridad, contexto, especificidad, ejemplos, permiso para decir "no sé") y cuatro avanzadas (prefill, cadena de pensamiento, control de formato de salida, encadenamiento de prompts). Refleja las recomendaciones por generación de modelo: Claude 4.x requiere menos manipulación de etiquetas XML y role-play que los modelos anteriores.

## Cuándo usarla
- Los prompts devuelven respuestas genéricas o fuera de tema
- Claude parece estar inventando información (alucinaciones)
- El formato de salida (JSON, prosa, listas) es inconsistente
- Una tarea compleja no se resuelve de un solo intento
- Necesitas optimizar el costo y la latencia de la API reformulando los prompts

## Cinco técnicas fundamentales

### 1. Sé explícito y claro
- Vague: `Create an analytics dashboard`
- Explicit: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`

### 2. Proporciona contexto y motivación
- Less effective: `NEVER use bullet points`
- More effective: `I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational.`

### 3. Sé específico
- Vague: `Create a meal plan for a Mediterranean diet`
- Specific: `Design a Mediterranean diet meal plan for pre-diabetic management. 1,800 calories daily, emphasis on low glycemic foods. List breakfast, lunch, dinner, and one snack with complete nutritional breakdowns.`

### 4. Usa ejemplos
Empieza con un solo ejemplo antes de pasar a varios. Es especialmente útil cuando importa el formato, el tono o patrones sutiles.
```
Here's an example of the summary style I want:

Article: [link]
Summary: EU passes comprehensive AI Act targeting high-risk systems. Key provisions include transparency requirements and human oversight mandates. Takes effect 2026.

Now summarize this article in the same style: [new link]
```

### 5. Da permiso para expresar incertidumbre
```
Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating.
```

## Cuatro técnicas avanzadas

### 1. Prefill de la respuesta
```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}
]
```

### 2. Cadena de pensamiento — básica / guiada / estructurada
Ejemplo estructurado:
```
Think before you write the email in <thinking> tags.
First, analyze what messaging would appeal to this donor.
Then, identify relevant program aspects.
Finally, write the personalized donor email in <email> tags, using your analysis.
```

### 3. Controla el formato de salida
Describe explícitamente la política de prosa, markdown o listas que deseas.

### 4. Encadenamiento de prompts
Divide tareas complejas en pasos secuenciales; pasa cada salida como entrada al siguiente prompt.

## Selección de técnicas

| Si necesitas… | Usa… |
|---|---|
| Formato de salida específico | Ejemplos, prefill o instrucciones de formato explícitas |
| Razonamiento paso a paso | Extended thinking (Claude 4.x) o cadena de pensamiento |
| Tarea compleja de múltiples etapas | Encadenamiento de prompts |
| Razonamiento transparente | Cadena de pensamiento con salida estructurada |
| Prevenir alucinaciones | Permiso para decir "no sé" |

## Antipatrones
- No sobre-ingenierices.
- No ignores los fundamentos.
- No asumas que la IA lee la mente.
- No uses todas las técnicas a la vez.
- No olvides iterar.
- No te apoyes en técnicas obsoletas (XML pesado / role-play).

## Resolución de problemas

| Síntoma | Solución |
|---|---|
| Demasiado genérico | Añade especificidad / ejemplos |
| Fuera de tema | Meta / contexto más explícitos |
| Formato inconsistente | Ejemplos o prefill |
| Demasiado complejo / poco fiable | Encadenamiento |
| Preámbulos innecesarios | Prefill / instrucción explícita de omitirlos |
| Inventa información | Permiso para decir "no sé" |
| Sugiere en vez de implementar | Verbos de acción explícitos |

## Fuente
Basado en [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) (2025-11-10). Consulta el original para obtener orientación autorizada.
