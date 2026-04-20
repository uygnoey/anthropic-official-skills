[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Preparando tu programa de seguridad para una ofensiva acelerada por IA

## ¿De qué trata este post?

Orientaciones del equipo de Ingeniería e Investigación de Seguridad de Anthropic sobre cómo adaptar un programa de seguridad a un entorno donde los modelos de IA encuentran, encadenan y explotan vulnerabilidades de forma rápida. El post se organiza en siete áreas de "qué hacer ahora" (brecha de parcheo, volumen de informes de vulnerabilidades, detección de errores antes del lanzamiento, auditoría de código existente, diseño orientado a la brecha, reducción de exposición, respuesta a incidentes), más una sección sobre cómo enviar informes de vulnerabilidades de alta calidad, recomendaciones para mantenedores en solitario o con equipos pequeños, y una tabla de referencia que mapea los temas a estándares (CISA KEV, EPSS, NIST SSDF, OWASP ASVS, SLSA, OpenSSF Scorecard, CISA Zero Trust Maturity Model, MITRE ATT&CK, NIST CSF 2.0, y más).

## ¿Cuándo es útil?

- Estás redefiniendo el alcance de un programa de seguridad existente para adaptarlo al ritmo de la explotación impulsada por IA
- Estás redactando actualizaciones de políticas de brecha de parcheo, gestión de vulnerabilidades o respuesta a incidentes
- Estás implementando revisión asistida por IA (similar a SAST) en CI y necesitas una ruta de despliegue responsable
- Estás a punto de enviar (o recibir) informes de vulnerabilidades asistidos por IA y quieres un estándar de calidad
- Lideras una organización pequeña o un proyecto de código abierto y necesitas una lista de acciones simplificada

## Puntos clave

- Cierra la brecha de parcheo: catálogo KEV de inmediato, EPSS para el resto, objetivo de 24 horas para los sistemas expuestos a internet, automatiza donde sea seguro
- Planifica un aumento de un orden de magnitud en los informes de vulnerabilidades; usa IA para el triaje, la deduplicación y la elaboración de parches
- Detecta errores antes de lanzar: SAST + revisión con IA en CI, pruebas de penetración en CD, asegura la cadena de compilación (SLSA), Secure by Design, prioriza lenguajes seguros para la memoria
- Audita el código existente: prioriza parsers, límites de autenticación, rutas accesibles desde internet y código heredado
- Diseña orientado a la brecha: zero trust, identidad vinculada al hardware, tokens de corta duración, reemplaza los controles de "fricción" por barreras reales
- Reduce e inventaría la exposición; retira servicios sin propietario; ejecuta red-teaming externo autónomo
- Acorta la respuesta a incidentes con un agente de triaje al frente de la cola, métricas de tiempo de permanencia, IA como escriba y procedimientos de cambio de emergencia acordados de antemano
- Escribe informes de vulnerabilidades asistidos por IA que un humano haya verificado y esté dispuesto a firmar
- Todo se mapea limpiamente sobre los controles existentes de SOC 2 / ISO 27001

## Recursos incluidos

- `skills/closing-the-patch-gap/SKILL.md` — patrón reutilizable de priorización y despliegue para la disciplina de brecha de parcheo
- `skills/writing-quality-vuln-reports/SKILL.md` — lista de verificación y autocomprobación para informes de vulnerabilidades asistidos por IA
- `agents/security-triage-agent.md` — agente de triaje con herramienta de consulta SIEM (mencionado en el post)
- `agents/vulnerability-scanning-agent.md` — agente aislado para escanear parsers / autenticación / rutas accesibles (mencionado en el post)
- `agents/external-red-team-agent.md` — agente autónomo de red-team externo contra tu propio perímetro (mencionado en el post)
- `guides/security-program-playbook.{en,ko,es,ja}.md` — el playbook completo de despliegue de las 7 áreas con referencias a estándares, en los cuatro idiomas

## Fuente

Basado en [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (publicado el 2026-04-10).
