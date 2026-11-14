"""Guardado seguro de archivos Markdown."""

import os
from pathlib import Path

CARPETA_SALIDA = Path("salida")


def guardar_markdown(nombre_archivo, contenido):
    """Guarda contenido dentro de salida/ y devuelve un diccionario con el resultado."""
    # Etapa 1: validar el nombre
    if not isinstance(nombre_archivo, str) or nombre_archivo.strip() == "":
        return {"ok": False, "error": "el nombre del archivo no puede estar vacío"}

    if not isinstance(contenido, str):
        return {"ok": False, "error": "el contenido debe ser texto"}

    if "\\" in nombre_archivo:
        return {"ok": False, "error": "el nombre no puede incluir carpetas"}

    ruta = Path(nombre_archivo)

    if ruta.is_absolute():
        return {"ok": False, "error": "no se permiten rutas absolutas"}

    if ".." in ruta.parts or ruta.name != nombre_archivo:
        return {"ok": False, "error": "el nombre no puede incluir carpetas ni '..'"}

    if ruta.suffix != ".md":
        return {"ok": False, "error": "el archivo debe terminar en .md"}

    # Etapa 2: preparar las rutas
    destino = CARPETA_SALIDA / nombre_archivo
    temporal = CARPETA_SALIDA / (nombre_archivo + ".tmp")

    # Etapa 3: escribir sin dejar archivos parciales
    try:
        CARPETA_SALIDA.mkdir(parents=True, exist_ok=True)
        temporal.write_text(contenido, encoding="utf-8")
        os.replace(temporal, destino)
    except OSError as error:
        temporal.unlink(missing_ok=True)
        return {"ok": False, "error": f"no se pudo guardar el archivo: {error}"}

    return {"ok": True, "ruta": destino.as_posix()}
