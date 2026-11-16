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

# Ejecutar la aplicación después de configurar .env
docker run --rm -it --user "$(id -u):$(id -g)" --env-file .env -v "$PWD:/workspace" -w /workspace \
  "$AGENTS_IMAGE" python main.py
```

La prueba de la extensión opcional se ejecuta con `python -m pytest -q pruebas/test_flujo.py`,
usando el mismo comando Docker y sin el filtro `-k`.

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
