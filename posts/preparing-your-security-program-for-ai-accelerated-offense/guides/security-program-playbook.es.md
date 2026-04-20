[English](./security-program-playbook.en.md) · [한국어](./security-program-playbook.ko.md) · [Español](./security-program-playbook.es.md) · [日本語](./security-program-playbook.ja.md)

# Guía de operaciones de seguridad para la ofensa acelerada por IA

Una guía de implementación consolidada, destilada del artículo del 10 de abril de 2026 [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) escrito por los equipos de Ingeniería de Seguridad e Investigación de Anthropic. Las recomendaciones del artículo se aplican directamente a los controles existentes de SOC 2 e ISO 27001. Nada de lo aquí expuesto es contenido inventado.

## Contexto

La IA está cambiando la velocidad a la que se descubren y explotan las vulnerabilidades. Esa misma semana, Anthropic anunció Project Glasswing, que utiliza Claude Mythos Preview para la ciberseguridad defensiva. En los próximos 24 meses, una enorme cantidad de bugs que permanecieron inadvertidos —posiblemente durante años— serán encontrados por modelos de IA y encadenados en exploits funcionales. Los defensores que adopten herramientas de IA también podrán moverse más rápido. A continuación se presentan las siete áreas de "qué hacer ahora" con orientación práctica, seguidas de consejos sobre la calidad de los informes y simplificaciones para equipos pequeños.

## 1. Cerrar la brecha de parches

Los modelos de IA son muy eficaces para reconocer las firmas de vulnerabilidades ya parcheadas en sistemas sin parchear. Invertir un parche para convertirlo en un exploit funcional es un análisis mecánico en el que estos modelos destacan, por lo que la ventana entre la publicación de un parche y la disponibilidad de un exploit se está reduciendo.

- Aplique parches de inmediato a todo lo que figure en el **catálogo CISA Known Exploited Vulnerabilities (KEV)**. Cualquier elemento de esta lista que sea accesible desde una red debe tratarse como una emergencia.
- Use **EPSS** (Exploit Prediction Scoring System) para priorizar el resto; proporciona una probabilidad actualizada diariamente de que un CVE sea explotado en los próximos 30 días.
- Reduzca el tiempo hasta el parche en sistemas expuestos a internet: **dentro de las 24 horas** siguientes a la disponibilidad de un exploit; en pocos días para otras vulnerabilidades.
- Automatice la implementación de parches y los reinicios cuando una actualización automática que cause una interrupción sea un riesgo aceptable. Los pasos de aprobación manual añaden demoras, y **el retraso es ahora el principal riesgo**.

**Consejo práctico.** La mayoría de los proveedores de nube y SO ya incluyen automatización de parches; habilitarla es a menudo un simple cambio de configuración. Para imágenes de contenedores y manifiestos de dependencias, varios escáneres de código abierto se ejecutan como un único paso en CI y anotan los CVE con datos de KEV y EPSS, de modo que la priorización ya está integrada.

→ Consulte la habilidad reutilizable [closing-the-patch-gap](../skills/closing-the-patch-gap/SKILL.md).

## 2. Prepararse para gestionar un volumen mucho mayor de informes de vulnerabilidades

El proceso de gestión de vulnerabilidades debe planificar muchos más parches, tanto de proveedores como de proyectos upstream.

- Planifique un **aumento de un orden de magnitud en el volumen de hallazgos.** Si sus reuniones de seguridad todavía giran en torno a una hoja de cálculo y una reunión semanal, es poco probable que pueda mantenerse al día.
- Verifique la seguridad de sus dependencias de código abierto. Use **OpenSSF Scorecard**; se ejecuta en CI y marca paquetes sin mantenimiento y señales ausentes (protección de ramas, cobertura de fuzzing, versiones firmadas, actividad de los mantenedores).
- Aplique las mismas expectativas a sus proveedores mediante la gestión de riesgos de terceros: pregunte cómo se están preparando para los plazos de exploit acelerados y si están analizando su propio código.

**Consejo práctico.** Explore herramientas que evalúen la accesibilidad del código vulnerable. Construya procesos automatizados que entreguen nuevas actualizaciones de forma continua, con pruebas de regresión para ganar confianza en la implementación rápida.

**Puntos de apalancamiento de IA en la gestión de vulnerabilidades:**
- *Acelerar el triaje.* Un modelo de frontera puede deduplicar hallazgos, estimar la exposición a partir del conocimiento de activos y redactar tickets de remediación con las rutas de código afectadas ya identificadas.
- *Verificación de redundancia de dependencias.* Las bases de código grandes tienden a acumular múltiples bibliotecas que hacen lo mismo (varios clientes HTTP; varios analizadores JSON). Dirigir un LLM a un archivo de bloqueo y preguntarle qué dependencias se superponen (y qué aspecto tendría la consolidación) es un ejercicio de una hora que a menudo da resultados.
- *Automatización de actualizaciones.* Los modelos de frontera pueden generar parches junto con informes de vulnerabilidades, probarlos y aceptar parches upstream mientras validan que las pruebas pasen.
- *AI vendoring.* Para dependencias pequeñas con puntuación baja en OpenSSF Scorecard y sin mantenimiento activo, considere que un LLM reimplemente únicamente la funcionalidad que realmente usa.

## 3. Encontrar bugs antes de publicar el código

- Añada **análisis estático y revisión de código asistida por IA** al CI; bloquee las fusiones en hallazgos de alta confianza. Si los falsos positivos hacen esto impracticable, corrija las herramientas, no la puerta.
- **OWASP ASVS** define qué significa "aprobar" en tres niveles de rigor.
- Añada **pruebas de penetración automatizadas** a la entrega continua; ejecute contra el entorno de staging los mismos análisis que los atacantes ejecutarán contra producción.
- **Proteja el pipeline de construcción.** El marco **SLSA** proporciona un camino gradual. OpenSSF publica un flujo de trabajo reutilizable de GitHub Actions que produce atestaciones SLSA Level 3, lo cual requiere significativamente menos trabajo del que sugiere la especificación SLSA.
- Adopte las prácticas **Secure by Design** como mínimo (el compromiso de CISA: MFA por defecto; sin contraseñas predeterminadas; reporte de vulnerabilidades transparente).
- Prefiera **lenguajes seguros para memoria** (Rust, Go, entornos de ejecución gestionados) para el código nuevo. El código C/C++ existente no necesita reescribirse, pero el código nuevo en C/C++ debería requerir una justificación. Las reescrituras asistidas por IA son cada vez más viables.

**Consejo práctico.** Las herramientas SAST con conjuntos de reglas de OWASP Top 10 y específicas por lenguaje están ampliamente disponibles, tanto de código abierto como integradas en plataformas de alojamiento de código. CodeQL en GitHub es el punto de partida más habitual.

**Puntos de apalancamiento de IA en el momento de construcción:**
- *Análisis de vulnerabilidades con IA.* Analice su propio código y sistemas con el mismo tipo de modelo que usaría un atacante, antes de que lo hagan ellos. Requiere un agente aislado, un paso de verificación para filtrar el ruido y una vía hacia el proceso de triaje existente. **Si va a implementar una sola cosa de esta sección, implemente esto.** → Consulte el [vulnerability-scanning-agent](../agents/vulnerability-scanning-agent.md).
- *Generación de parches.* Un modelo de frontera normalmente puede proponer un parche para un hallazgo de SAST o escáner. El trabajo del desarrollador pasa de "entender el bug y escribir una corrección" a "verificar que la corrección propuesta es correcta"; lo segundo es más rápido. El mismo enfoque aplica a la migración a lenguajes seguros para memoria: porte un módulo C autónomo a Rust con pruebas y valide la equivalencia.

## 4. Encontrar las vulnerabilidades ya presentes en su código

La mayor parte del código de producción en ejecución prolongada ha sido revisado muchas veces por humanos, pero nunca examinado por un modelo de frontera. El análisis proactivo identifica vulnerabilidades al alcance de los LLM modernos antes de que los atacantes las descubran.

- **Priorice por exposición.** Comience con el código que analiza entradas no confiables, aplica decisiones de autenticación o es accesible desde internet.
- **Incluya el código heredado.** El código anterior a las prácticas de revisión actuales suele ser el que menos escrutinio reciente ha tenido y el que más puede ganar con un análisis nuevo.
- **Presupueste para la remediación.** Un análisis de modelo sobre código antiguo suele producir menos hallazgos que una implementación de SAST, pero una proporción mayor de ellos son reales. Planifique el tiempo de ingeniería.

**Consejo práctico.** Seleccione un servicio orientado a internet con pocos propietarios actuales y analice su manejo de entradas y lógica de autenticación. Ejecute el agente en aislamiento, añada un paso de verificación y actúe sobre los hallazgos confirmados. Un servicio bien ejecutado es una base razonable para estimar el costo del programa más amplio.

## 5. Diseñar para la brecha

Las mitigaciones cuyo valor proviene de la fricción (hacer que un ataque sea tedioso) son menos eficaces contra adversarios capaces de superar cualquier tedio. Favorezca los controles que se mantienen ante una paciencia ilimitada del atacante.

- **Adopte una arquitectura de confianza cero.** Autentique y autorice cada solicitud entre servicios como si viniera de internet. Tanto el **CISA Zero Trust Maturity Model** como los **NCSC zero trust principles** ofrecen rutas de adopción gradual.
- **Vincule el acceso al hardware verificado**, no a las credenciales. Los sistemas de producción y las herramientas internas sensibles solo deben ser accesibles desde dispositivos de empleados gestionados con identidad de hardware certificada, junto con **2FA resistente al phishing (FIDO2 / passkeys)**. Las credenciales robadas por sí solas nunca deben ser suficientes. Incluso las llamadas entre servicios deben basarse en identidad de hardware.
- **Aísle los servicios por identidad.**
- **Reemplace los secretos de larga duración con tokens de corta duración y alcance limitado** emitidos por un proveedor de identidad. Las claves API estáticas y las credenciales embebidas son de las primeras cosas que encontrará un atacante con análisis de código asistido por modelos.

**Consejo práctico.** La confianza cero completa es un programa de varios años, pero un **proxy de acceso con reconocimiento de identidad** coloca el acceso verificado por dispositivo y con restricción de MFA frente a los servicios internos sin necesidad de rediseñarlos. Todos los principales proveedores de nube ofrecen una opción nativa, además de alternativas de código abierto y comerciales. Para los secretos, mueva la credencial más ampliamente compartida a un almacén de secretos gestionado y róte­la; eso es una función forzadora útil para el resto.

## 6. Reducir e inventariar lo que se expone

Dos principios: no se puede defender lo que no se conoce, y una superficie expuesta menor significa menos objetivos de ataque.

- Mantenga un **inventario actualizado** de cada host, servicio y endpoint de API expuesto a internet. Inclúyalos en pentests y ejercicios de red team.
- **Decomisione los sistemas sin uso.** Los servicios heredados sin propietario claro suelen estar también sin parchear.
- **Minimice** lo que expone cada servicio. Denegación predeterminada para el tráfico de red entrante; limite la superficie de la API a lo estrictamente necesario.

**Consejo práctico.** Los índices de análisis de internet están disponibles públicamente: consulte uno con sus propios rangos de IP y dominios para ver lo que ve el reconocimiento de un atacante. Para los activos en la nube, ya existen herramientas de inventario nativas (**AWS Config, Azure Resource Graph, GCP Asset Inventory**); el trabajo está en consultarlas.

**Puntos de apalancamiento de IA para la exposición:**
- *Eliminar código y sistemas obsoletos.* Un modelo con acceso de lectura a una base de código y los registros de tráfico puede listar los endpoints que no tienen llamadores y no han recibido tráfico; a partir de ahí, explicar qué implicaría eliminar cada uno.
- *Red team externo autónomo.* Dirija un agente ofensivo de IA contra su propio perímetro desde el exterior, sin credenciales ni acceso al código fuente. Detecta lo que el análisis de código fuente no ve: hosts olvidados, interfaces de administración expuestas, credenciales predeterminadas, almacenamiento mal configurado. Ejecútelo con la misma cadencia que la actualización del inventario. → Consulte el [external-red-team-agent](../agents/external-red-team-agent.md).

## 7. Reducir el tiempo de respuesta ante incidentes

Los exploits pueden aparecer pocas horas después de un parche. Los procesos de respuesta medidos en días son demasiado lentos.

- **Coloque un modelo al frente de la cola de alertas.** Cada alerta entrante recibe una investigación inicial automatizada antes de que la vea un humano. Un "agente de triaje" con acceso de solo lectura al SIEM dirige la atención hacia las alertas que más necesitan juicio humano. → Consulte el [security-triage-agent](../agents/security-triage-agent.md).
- **Instrumente primero el tiempo de permanencia y la cobertura.** Estas son las dos métricas que más puede mover la automatización de IA, y las que más importan cuando se reducen las ventanas de exploit.
- **Automatice las tareas administrativas relacionadas con los incidentes.** Los modelos toman notas, capturan artefactos, siguen pistas de investigación en paralelo y redactan el postmortem. Los **humanos** toman las decisiones de contención, divulgación y comunicación con clientes. La velocidad de decisión humana nunca debe estar limitada por la recopilación de evidencias o la redacción de informes.
- **Deje que los modelos impulsen el ciclo de detección** — ingiriendo inteligencia de amenazas, generando detecciones candidatas, realizando búsquedas activas y ajustando lo que se activa.
- **Realice un ejercicio de mesa para cinco incidentes simultáneos.** El supuesto estándar de "un CVE crítico el lunes" puede ser imprudente dadas las capacidades de la IA. Haga una prueba de estrés con cinco incidentes en la misma semana.
- **Mapee la cobertura de detección contra MITRE ATT&CK.** Un vocabulario estándar de técnicas de atacantes. Saber qué puede y qué no puede detectar es más útil que un objetivo genérico de "mejorar la detección". Priorice la cobertura de movimiento lateral y acceso a credenciales.
- **Establezca procedimientos de cambio de emergencia de antemano.** Un ciclo de aprobación de cambios de dos semanas para parches de producción es en sí mismo un riesgo de seguridad. Lo mismo aplica para las acciones de contención (desconectar un servicio, rotar una credencial, bloquear una ruta de red). Decida de antemano quién autoriza y con qué rapidez.

**Consejo práctico.** Seleccione una regla ruidosa con una tasa de falsos positivos conocidamente alta. Conecte un modelo de frontera a su flujo de alertas con acceso de solo lectura, haga que produzca una disposición estructurada para cada disparo, y mida el acuerdo con un revisor humano durante dos semanas. Si el acuerdo es tolerable, expándalo a la siguiente regla. No intente automatizar toda la cola de una vez. Por separado, **Atomic Red Team** es una biblioteca de código abierto de pruebas pequeñas y seguras mapeadas a técnicas de ATT&CK; ejecutar un puñado y comprobar cuáles detectó realmente el registro existente es un ejercicio de una tarde que produce un mapa de cobertura concreto.

## Envío de informes de vulnerabilidades a terceros

Si está analizando código (sus propias dependencias, proyectos de código abierto, productos de proveedores) e informando upstream, la calidad del informe determina si alguien actúa sobre el hallazgo. Los mantenedores de código abierto ya reciben grandes volúmenes de informes automatizados de baja calidad, y muchos ignoran cualquier cosa que parezca generada por IA. **Un informe solo debe enviarse cuando un humano lo ha verificado y está dispuesto a firmarlo con su nombre.**

Consulte la habilidad reutilizable [writing-quality-vuln-reports](../skills/writing-quality-vuln-reports/SKILL.md) para la lista de verificación de envío y la autoevaluación.

## Si no tiene un equipo de seguridad

La mayor parte de los consejos anteriores asume una función de seguridad dedicada. Desarrolladores en solitario, mantenedores de código abierto y organizaciones pequeñas: los riesgos aplican igualmente, pero las acciones son más simples.

- **Active las actualizaciones automáticas** para el SO, el navegador y todas las aplicaciones que lo ofrezcan. Es la acción individual más eficaz disponible; no requiere esfuerzo continuo.
- **Prefiera los servicios gestionados al autoalojamiento.** Dejar que un proveedor con equipo de seguridad gestione la base de datos, la autenticación y el correo electrónico transfiere la carga de los parches a ellos. Suele ser más barato que un solo incidente.
- **Use passkeys o llaves de seguridad de hardware** en todas las cuentas que las admitan. Los códigos SMS pueden interceptarse; las contraseñas se reutilizan; una llave de hardware no puede ser suplantada mediante phishing.
- **Active las herramientas de seguridad gratuitas** de su plataforma de alojamiento de código. Dependabot, el análisis de secretos y CodeQL de GitHub son gratuitos para repositorios públicos y detectan una parte significativa de lo que detectan las herramientas empresariales. Habilitarlos lleva minutos.
- Si mantiene un proyecto de código abierto, **publique un SECURITY.md** indicando a quién contactar y qué esperar. El análisis asistido por IA significa más informes: una recepción clara ayuda a distinguir la señal del ruido y señala a los informadores de buena fe que su esfuerzo no será en vano.

## Tabla de referencias

| Tema | Referencia |
|---|---|
| Priorización de parches | CISA KEV Catalog, FIRST EPSS, CISA BOD 22-01 |
| Controles de base | ACSC Essential Eight, CISA CPGs, CIS Controls v8, NCSC 10 Steps |
| Desarrollo seguro | NIST SSDF (SP 800-218), OWASP ASVS, OWASP SAMM, CISA Secure by Design |
| Seguridad de memoria | CISA/NSA Memory Safe Roadmaps |
| Cadena de suministro e integridad de construcción | SLSA, OpenSSF Scorecards, CISA SBOM resources, NIST SP 800-161 |
| Confianza cero | CISA Zero Trust Maturity Model, NIST SP 800-207, NCSC Zero Trust Principles |
| Detección y respuesta | MITRE ATT&CK, MITRE D3FEND |
| Marco del programa | NIST Cybersecurity Framework 2.0, NCSC Cyber Assessment Framework |

## Agradecimientos

El artículo fuente fue escrito por miembros de los equipos de Ingeniería de Seguridad e Investigación de Anthropic, incluidos Donny Greenberg, Jason Clinton, Michael Moore, Abel Ribbink y Jackie Bow, con contribuciones de Jannet Park, Gabby Curtis y Stuart Ritchie.

## Fuente

[Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (publicado el 2026-04-10).
