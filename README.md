# Agentes de IA con Python

Documentación de la aplicación, situada junto a `main.py`, con las decisiones,
los ejemplos y la reflexión del proyecto.

La imagen creó los archivos iniciales con `iniciar-proyecto`. Consulta la
[guía de trabajo con Docker y VS Code](docs/trabajar-con-docker.md).

## Descripción

Esta aplicación genera guías de estudio de Python en formato Markdown.
Para hacerlo utiliza tres agentes de IA que trabajan en secuencia: el
explicador presenta el tema, el diseñador propone una práctica basada en
esa explicación y el revisor corrige el borrador completo. Antes de
guardar la guía en la carpeta `salida/`, una función de Python valida
que tenga la estructura requerida.

## Antes de comenzar

La imagen Docker proporcionada contiene Python, ADK y las dependencias necesarias.

Configura la imagen pública preparada para este proyecto una vez en cada
terminal y descárgala:

```bash
export AGENTS_IMAGE="ghcr.io/hbtn-edu/ai-agents-python:0.4.0"
docker pull "$AGENTS_IMAGE"
```

Ubícate en la carpeta local creada al inicializar el proyecto. `"$PWD"` comparte la carpeta
actual con el contenedor para que puedas editarla con tus herramientas habituales.

```bash
# Comprobar Python, ADK y el entorno sin consumir API
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m runtime.diagnostico --sin-api

# Ejecutar las pruebas básicas del starter pack
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" \
  python -m pytest -q pruebas/test_entorno.py pruebas/test_runtime.py

# Ejecutar todas las pruebas públicas de las tareas obligatorias
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m pytest -q -k 'not extension'

# Ejecutar todas las pruebas, incluida la extensión opcional
docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m pytest -q

# Ejecutar la aplicación después de configurar .env
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python main.py
```

## Configuración segura de Gemini

1. Abre [Google AI Studio](https://aistudio.google.com/apikey) e inicia sesión.
2. Crea una clave en la sección de claves de API. Si la cuenta requiere asociar
   un proyecto de Google Cloud, sigue la
   [guía de creación y gestión de claves](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419).
3. Edita el `.env` creado al inicializar y completa `GOOGLE_API_KEY` con la clave.
4. Conserva `GEMINI_MODEL=gemini-3.5-flash` y las demás variables del archivo.
5. Comprueba con `git check-ignore .env` que Git ignora el archivo.

```bash
git check-ignore .env

docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m runtime.diagnostico --sin-api
```

La siguiente comprobación realiza una llamada real y consume cuota. Ejecútala
una vez para verificar el acceso:

```bash
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python -m runtime.diagnostico --con-api
```

El diagnóstico informa si la clave está configurada, pero nunca muestra su
valor ni una parte de ella.

### Si el servicio no está disponible

El modelo configurado es `gemini-3.5-flash`, probado con este starter pack.
Si aparece `503 UNAVAILABLE` o «El servicio no está disponible», termina esa
ejecución, espera al menos un minuto y vuelve a ejecutar manualmente el mismo
comando una sola vez. Si vuelve a fallar, registra el modelo, la hora y el
mensaje, y consulta el [estado del servicio](https://aistudio.google.com/status).
Mientras se restablece, el modo simulado permite comprobar las operaciones locales.

Ante un error de cuota (`429`), detén las llamadas y revisa los límites de la
cuenta antes de una nueva ejecución. Consulta la
[guía de solución de problemas](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=es-419),
solamente «Estrategia de reintentos» y «Verifica si tienes el modelo correcto».

## Modo simulado

Las respuestas fijas incluidas permiten comprobar el flujo sin consumir API.
La calidad de las respuestas a temas diferentes se verifica con ejecuciones reales.

```bash
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -e MODO_SIMULADO=1 \
  -v "$PWD:/workspace" -w /workspace "$AGENTS_IMAGE" python main.py
```

## Estructura

- `main.py`: flujo secuencial (`ejecutar_flujo`) y entrada del programa.
- `agentes/`: definición de los tres agentes.
- `herramientas/`: guardado seguro y validación determinista.
- `runtime/`: infraestructura de ejecución suministrada.
- `pruebas/`: pruebas públicas que no consumen API.
- `ejemplos/`: respuestas fijas, guías de ejemplo y evidencias de las pruebas manuales.
- `probar_errores.py`: pruebas manuales de errores simulados, sin usar la API.
- `salida/`: archivos generados, ignorados por Git.

## Agentes

La aplicación usa tres agentes, cada uno con una responsabilidad:

| Agente | Archivo | Qué recibe | Qué produce |
| --- | --- | --- | --- |
| `explicador_python` | `agentes/explicador.py` | El tema | Una explicación breve, un ejemplo en Python y un error frecuente |
| `disenador_practica` | `agentes/disenador_practica.py` | El tema y la explicación | Un ejercicio, tres criterios de aceptación y una pista |
| `revisor_python` | `agentes/revisor.py` | El borrador completo | La guía final con la sección `## Revisión` |

## Herramientas

Son funciones de Python deterministas: ante la misma entrada devuelven siempre el mismo resultado.

| Herramienta | Archivo | Qué hace |
| --- | --- | --- |
| `validar_guia` | `herramientas/validacion.py` | Comprueba el título, las tres secciones, el bloque de código Python y la ausencia de contenido sensible. Devuelve la lista de requisitos faltantes |
| `guardar_markdown` | `herramientas/archivos.py` | Guarda solo archivos `.md` dentro de `salida/`, en UTF-8. Rechaza rutas absolutas, subcarpetas y `../`, y no deja archivos parciales |

## Flujo

`ejecutar_flujo`, en `main.py`, coordina las etapas en este orden:

```
tema → explicador → diseñador → borrador → revisor → guía final → validación → archivo Markdown
```

Una ejecución normal realiza tres invocaciones, una por agente. La guía se guarda
solamente si pasa la validación.

Con `permitir_correccion=True`, si la guía no supera la validación se hace una única
invocación adicional al revisor con la guía y la lista de faltantes. La guía se valida
de nuevo y se guarda solo si esa segunda versión es válida. Hay cuatro invocaciones
como máximo.

## Ejemplo de ejecución

```bash
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python main.py
```

```
Tema de Python: listas
Guía guardada en: salida/guia_listas.md
```

Guías generadas con Gemini y verificadas con `validar_guia`:

- [Guía de listas](ejemplos/guia_listas.md)
- [Guía de funciones](ejemplos/guia_funciones.md)

## Errores frecuentes

| Mensaje | Causa | Qué hacer |
| --- | --- | --- |
| `El tema no puede estar vacío.` | No se escribió un tema | Volver a ejecutar e ingresar un tema |
| `Configuración incompleta: ...` | Falta `GOOGLE_API_KEY` o `GEMINI_MODEL`, o no se usó `--env-file .env` | Revisar `.env` y el comando |
| `Límite de cuota: ...` | Se alcanzó el límite de la cuenta (429) | No reintentar; revisar los límites |
| `Servicio no disponible: ...` | El servicio no responde (503 o red) | Esperar al menos un minuto y reintentar manualmente una sola vez |
| `Respuesta vacía: ...` | Un agente no produjo texto | Volver a ejecutar más tarde |
| `La guía no es válida. Faltan: ...` | La guía final no tiene la estructura requerida | Revisar las instrucciones del agente revisor |
| `No se pudo guardar la guía: ...` | Fallo de escritura en `salida/` | Revisar permisos y espacio en disco |

Ante un error, el programa termina sin volver a invocar al modelo y sin guardar
contenido parcial. Los mensajes nombran la variable que falta, nunca su valor.

## Limitaciones

- Las respuestas de los agentes varían entre ejecuciones: el mismo tema produce guías con redacción y formato distintos.
- `validar_guia` comprueba la estructura, no el contenido: no detecta una explicación incorrecta ni una errata.
- El revisor mejora el borrador pero no es infalible: en las guías de ejemplo dejó pasar palabras pegadas, como «enpantalla» y «eimprímelo».
- Al corregir, el revisor puede reescribir la práctica y perder los criterios de aceptación o la pista.
- Si se pide dos veces el mismo tema, la guía nueva reemplaza a la anterior en `salida/`.
- La aplicación depende de la disponibilidad y la cuota de Gemini; el modo simulado solo comprueba el recorrido.

## Recomendaciones de seguridad y privacidad

- Utiliza datos ficticios y limita el contexto enviado a la información necesaria.
- Mantén la clave en `.env`, excluida de Git, documentación, capturas y mensajes.
- Si una clave se expone, revócala y reemplázala.
- Las guías de ejemplo no contienen datos personales: usan nombres y valores ficticios.

## Reflexión

### 1. ¿Qué diferencia hay entre una llamada directa a un modelo y un agente?

Una llamada directa envía un texto y recibe una respuesta, sin un rol ni reglas
fijas. Un agente es un modelo con nombre, descripción e instrucciones permanentes:
en este proyecto las reglas de cada agente se definen una sola vez en `instruction`,
y lo que cambia en cada uso es el mensaje con el tema o el borrador.

### 2. ¿Qué responsabilidad tiene cada agente y cada herramienta?

El explicador presenta el tema con un ejemplo y un error frecuente; el diseñador
propone una práctica con tres criterios y una pista a partir de esa explicación;
el revisor comprueba la coherencia del borrador y entrega la guía final.
`validar_guia` verifica que la estructura esté completa y `guardar_markdown`
escribe el archivo solo en `salida/` y solo con un nombre seguro.

### 3. ¿Qué parte es determinista y cuál puede variar?

Las herramientas son deterministas: la misma guía recibe siempre el mismo resultado
de validación. Los agentes son generativos: en mis pruebas el mismo explicador usó
negritas para un tema y encabezados para otro, y al repetir el tema «listas» la
guía salió redactada de otra forma.

### 4. ¿Por qué se valida con Python además de usar un revisor?

Porque cumplen funciones distintas. El revisor entiende el sentido: detectó una
práctica sobre diccionarios en una guía de listas, algo que `validar_guia` no
puede ver. Pero el revisor puede fallar o variar, y dejó pasar erratas. Las reglas
que deben cumplirse exactamente, como la presencia de las secciones, no pueden
depender de una respuesta que puede cambiar.

### 5. ¿Qué cambiaría al utilizar otro proveedor o un modelo local?

Cambiaría la configuración en `.env` (proveedor, modelo y credenciales) y la
infraestructura de `runtime/`, que hoy admite solamente Gemini. Las herramientas
y el flujo no cambiarían, porque no dependen del modelo. Las instrucciones de los
agentes habría que volver a probarlas, ya que otro modelo puede interpretarlas
distinto. Con un modelo local no habría cuota ni clave y los datos no saldrían
del equipo, pero haría falta hardware suficiente y la calidad podría ser menor.