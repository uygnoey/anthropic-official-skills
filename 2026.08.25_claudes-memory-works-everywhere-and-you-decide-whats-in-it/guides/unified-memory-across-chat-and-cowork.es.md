[English](./unified-memory-across-chat-and-cowork.en.md) · [한국어](./unified-memory-across-chat-and-cowork.ko.md) · **Español** · [日本語](./unified-memory-across-chat-and-cowork.ja.md)

# Memoria unificada entre el chat y Cowork

## Qué cambió

Desde el 2026-08-25, la memoria que usas en el chat es la misma que usa Claude Cowork. Trabajes
donde trabajes con Claude, parte de lo que ya sabe sobre ti.

Junto a ese cambio llegan otros tres:

1. **La memoria se actualiza mientras conversas.** Claude añade temas a la memoria durante la
   conversación, en lugar de resumirla cuando termina.
2. **Las memorias guardadas son visibles y editables.** Todo lo que Claude recuerda aparece como
   una lista de archivos breves en **Temas**, dentro de los ajustes de Memoria.
3. **Tú decides el límite.** Los asuntos sensibles quedan excluidos por defecto y pueden
   activarse; un pequeño conjunto de categorías no se almacena en ningún caso.

## Cómo se comporta la memoria compartida

Es un único almacén, leído y escrito desde ambas superficies:

- Cuando Cowork ejecuta una tarea en la nube, lo que Claude recuerda de tus chats está ahí.
- Lo que surge durante una tarea de Cowork vuelve al chat.
- El contexto acumulado durante meses de conversaciones —prioridades del Q3, estado de los
  proyectos— está presente en el momento en que le pasas una tarea a Cowork.

En la práctica, esto elimina el paso de volver a informar al delegar trabajo:

- Pide a Cowork un borrador de actualización para tu responsable y ya sabe quién es y cómo le
  gusta que se redacten.
- Piensa la agenda de una conferencia en el chat: el documento de presupuesto y logística que
  construya Cowork conocerá el número de asistentes, la ciudad y los ponentes.
- Explica una vez cómo define tu equipo sus métricas y todas las presentaciones de revisión
  trimestral posteriores las usarán sin volver a informarle.

## Revisar y corregir lo almacenado

Abre **Configuración > Memoria** y mira en **Temas**. Cada entrada es un archivo breve que puedes
leer, editar o eliminar.

Que los archivos sean cortos e independientes es lo que abarata la corrección: corrige el nombre
antiguo de tu empresa en un archivo y todas las conversaciones posteriores lo usarán bien, en
ambas superficies. Edita el archivo cuando solo una parte esté desactualizada; elimínalo cuando
el tema entero haya quedado obsoleto.

La memoria también puede pausarse o restablecerse en cualquier momento: pausa para un trabajo que
no debería condicionar conversaciones futuras y restablece cuando el contexto acumulado ya no se
corresponda con tu situación.

## Decidir sobre los temas sensibles

Por defecto, Claude no almacena temas de carácter personal o sensible: salud, raza, etnia,
creencias religiosas, política, identidad de género y otros ámbitos similares.

Lo que unas personas consideran sensible, otras lo consideran contexto útil para que Claude lo
recuerde. Si activas **"incluir temas sensibles en la memoria"**, Claude recordará cosas como una
alergia al gluten al sugerir recetas para la preparación semanal de comidas. Tres propiedades
importan para la decisión:

- **Es visible.** Verás un aviso cada vez que Claude guarde algo de estos temas.
- **Solo hacia adelante.** Claude guarda temas sensibles a partir de ese momento; nada anterior a
  la activación se guarda de forma retroactiva.
- **Es reversible.** Puedes desactivar el ajuste en cualquier momento.

### Lo que nunca se almacena

Con independencia de ese ajuste, Claude no almacena números de identificación sensibles (SSN,
números de documentos oficiales y similares), antecedentes penales, situación migratoria ni nada
que infrinja la Política de Uso Aceptable. Claude te avisará cuando no pueda actualizar la memoria
con esa información. El Centro de ayuda lo detalla.

## Disponibilidad y despliegue

| Plan | Memoria | Temas sensibles |
| --- | --- | --- |
| Free, Pro, Max | Activada por defecto, en web, escritorio y móvil | Desactivados por defecto |
| Team, Enterprise | Los administradores controlan la disponibilidad de la organización; desactivada para cada usuario hasta que la active | Desactivados por defecto |

En iOS y Android, actualiza a la última versión de la app para disponer de las novedades.

### Para administradores de Team y Enterprise

- La disponibilidad es una decisión de organización que tomas primero; después cada usuario
  activa la memoria por su cuenta.
- Guardar temas sensibles sigue desactivado por defecto, así que habilitar la memoria para la
  organización no introduce por sí solo información de salud, creencias o identidad en el almacén.
- Indica dónde están los controles —**Configuración > Memoria**— y que la lista de Temas se puede
  leer y editar, de modo que revisar lo almacenado forme parte del uso normal y no de una
  solicitud de soporte.

## Primeros pasos

1. Abre **Configuración > Memoria** y confirma que la memoria está activada (en Team y Enterprise,
   después de que tu administrador la habilite para la organización).
2. Lee la lista de **Temas** entera una vez. Corrige lo desactualizado; elimina lo obsoleto.
3. Decide de forma deliberada si activas los temas sensibles.
4. Explica una vez en el chat un contexto recurrente, pasa después una tarea relacionada a Cowork
   y comprueba que se ha trasladado.

## Fuente

- https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it (publicado el 2026-08-25)
