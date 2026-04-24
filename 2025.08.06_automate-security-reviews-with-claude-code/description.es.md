[English](./description.en.md) · [한국어](./description.ko.md) · **Español** · [日本語](./description.ja.md)

## ¿De qué trata este post?
Este post presenta revisiones de seguridad automatizadas en Claude Code, incluyendo el comando ad-hoc `/security-review` y una integración con GitHub Actions para revisar pull requests.

## ¿Cuándo es útil?
- Antes de hacer commit, para detectar vulnerabilidades comunes cuanto antes.
- En cada pull request, para señalar problemas y proponer correcciones dentro de tu flujo de CI.

## Puntos clave
- El comando `/security-review` puede revisar riesgos de inyección SQL, cross-site scripting (XSS), fallos de autenticación/autorización, manejo inseguro de datos y vulnerabilidades en dependencias.
- La GitHub Action puede comentar sobre los cambios en el PR y se puede configurar para reducir falsos positivos mediante reglas personalizadas.
- Después de identificar problemas, puedes pedirle a Claude Code que implemente las correcciones.

## Recursos incluidos
- Skill: `skills/security-review-automation/SKILL.md`

## Fuente
- https://claude.com/blog/automate-security-reviews-with-claude-code
