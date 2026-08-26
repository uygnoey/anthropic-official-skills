[English](./built-in-browser-rollout.en.md) · [한국어](./built-in-browser-rollout.ko.md) · **Español** · [日本語](./built-in-browser-rollout.ja.md)

# Desplegar el navegador integrado en Cowork

## Qué se ha lanzado

Claude ya tiene un navegador integrado en Claude Cowork en la aplicación de escritorio. Cuando una
tarea necesita usar un sitio web, se abre un navegador en el panel lateral y Claude navega por las
páginas, las lee, hace clic y escribe.

Es un navegador propio de Claude, no el tuyo. Se mantiene separado de tu navegación personal, y
Claude nunca ve tus pestañas, marcadores ni contraseñas.

## Quién lo recibe y cuándo

- **Pro, Max y Team:** despliegue a lo largo de la semana en macOS, Windows y Linux (beta).
- **No requiere configuración.** Encárgale a Claude una tarea que necesite la web y el navegador se
  abrirá en el panel lateral.
- **Empresa:** los administradores pueden activarlo de inmediato en **Organization settings →
  Cowork → Built-in browser**.

## Dónde se ejecuta el navegador

El navegador vive en la aplicación de escritorio. La web y el móvil pueden usarlo mientras la
aplicación de escritorio esté abierta y conectada. Quienes solo usan la web, sin la aplicación de
escritorio, siguen con Claude in Chrome.

Planifica en consecuencia: un flujo de trabajo que dependa del navegador integrado necesita una
aplicación de escritorio en marcha en algún sitio, aunque quien lo dirija esté en la web o en el
teléfono.

## Elegir el navegador por defecto

Cowork tiene ahora dos formas de actuar en la web, y el valor por defecto cambia según si ya usas
Claude in Chrome. Defínelo explícitamente en **Settings → Cowork → Preferred browser**.

Criterio del anuncio:

- **Navegador integrado** — para tareas web que deben avanzar mientras sigues siendo productivo en
  otra cosa: reunir investigación, recopilar facturas en portales de proveedores.
- **Claude in Chrome** — para páginas que ya tienes abiertas y con sesión iniciada: actualizar un
  CRM, vaciar una bandeja de entrada, editar un documento.

## Configurar los inicios de sesión

El navegador integrado empieza sin ninguna sesión. Los inicios de sesión se importan sitio por
sitio:

- **macOS:** desde Chrome, Edge o Firefox.
- **Windows y Linux:** desde Firefox.

Los sitios de banca, correo y SSO quedan excluidos por defecto salvo que los incluyas
explícitamente. Mantener ese valor por defecto es la forma más sencilla de acotar hasta dónde puede
llegar una tarea del navegador.

## Postura de seguridad

El navegador integrado está expuesto a la inyección de prompts: instrucciones ocultas en una página
que intentan desviar a Claude. Cuenta con las mismas salvaguardas que Claude in Chrome, incluidas
las comprobaciones de que las acciones se corresponden con la petición del usuario. Estas medidas
reducen el riesgo de forma significativa, pero no pueden eliminarlo.

Empieza por sitios web de confianza. Hay más orientación en la documentación de seguridad a la que
remite el anuncio.

## Lista de comprobación para el despliegue

1. Confirma la plataforma: macOS, Windows o Linux (beta), con la aplicación de escritorio instalada.
2. En una organización, actívalo en Organization settings → Cowork → Built-in browser.
3. Define el navegador preferido en Settings → Cowork → Preferred browser en lugar de aceptar el
   valor inferido.
4. Importa solo los inicios de sesión que necesiten las primeras tareas; deja excluidos banca,
   correo y SSO.
5. Empieza con sitios de confianza y tareas de bajo impacto —reunir investigación, recopilar
   facturas— antes de ampliar.

## Fuente

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
