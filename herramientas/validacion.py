"""Validación determinista de la estructura de una guía."""

import os

PREFIJO_TITULO = "# Guía de estudio:"
SECCIONES = ["## Explicación", "## Práctica", "## Revisión"]
MARCADOR_PRUEBA = "TRAINING_SECRET_TEST_VALUE"


def validar_guia(contenido):
    """Comprueba la estructura de una guía y devuelve los requisitos faltantes."""
    # Etapa 1: contenido vacío
    if not isinstance(contenido, str) or contenido.strip() == "":
        return {"valida": False, "faltantes": ["contenido no vacío"]}

    # Etapa 2: recorrer la guía línea por línea
    encabezados = []
    hay_bloque_python = False
    dentro_de_bloque = False
    bloque_es_python = False

    for linea in contenido.splitlines():
        texto = linea.strip()

        if texto.startswith("```"):
            if not dentro_de_bloque:
                dentro_de_bloque = True
                bloque_es_python = texto[3:].strip().lower() == "python"
            else:
                dentro_de_bloque = False
                if bloque_es_python:
                    hay_bloque_python = True
        elif not dentro_de_bloque and texto.startswith("#"):
            encabezados.append(texto)

    # Etapa 3: comparar con las reglas
    faltantes = []

    if not any(e.startswith(PREFIJO_TITULO) for e in encabezados):
        faltantes.append("título")

    for seccion in SECCIONES:
        if seccion not in encabezados:
            faltantes.append(seccion)

    if not hay_bloque_python:
        faltantes.append("bloque de código Python")

    clave = os.getenv("GOOGLE_API_KEY")
    if (clave and clave in contenido) or MARCADOR_PRUEBA in contenido:
        faltantes.append("contenido sensible")

    # Etapa 4: responder
    return {"valida": len(faltantes) == 0, "faltantes": faltantes}
    