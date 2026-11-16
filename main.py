"""Aplicación principal: coordina los agentes y las herramientas."""

import re
import unicodedata

from agentes.disenador_practica import crear_agente_disenador
from agentes.explicador import crear_agente_explicador
from agentes.revisor import crear_agente_revisor
from herramientas.archivos import guardar_markdown
from herramientas.validacion import validar_guia
from runtime.ejecutor import ejecutar_agente


def _nombre_archivo(tema):
    """Convierte el tema en un nombre de archivo simple, como guia_listas.md."""
    texto = unicodedata.normalize("NFKD", tema.lower())
    texto = texto.encode("ascii", "ignore").decode("ascii")
    texto = re.sub(r"[^a-z0-9]+", "_", texto).strip("_")
    return f"guia_{texto or 'tema'}.md"


def ejecutar_flujo(tema, ejecutar=ejecutar_agente, permitir_correccion=False):
    """Coordina los agentes usando un ejecutor reemplazable en las pruebas."""
    # Paso 1: rechazar un tema vacío antes de invocar agentes
    if not isinstance(tema, str) or tema.strip() == "":
        raise ValueError("El tema no puede estar vacío.")
    tema = tema.strip()

    # Paso 2: explicador
    explicacion = ejecutar(crear_agente_explicador(), f"Explica este tema de Python: {tema}")

    # Paso 3: diseñador, con el tema y la explicación
    mensaje_practica = f"Tema: {tema}\n\nExplicación previa:\n{explicacion}"
    practica = ejecutar(crear_agente_disenador(), mensaje_practica)

    # Paso 4: construir el borrador con las respuestas completas
    borrador = (
        f"# Guía de estudio: {tema}\n\n"
        f"## Explicación\n\n{explicacion}\n\n"
        f"## Práctica\n\n{practica}\n"
    )

    # Paso 5: revisor; su respuesta es la guía final
    guia_final = ejecutar(crear_agente_revisor(), borrador)

    # Paso 6: validar antes de guardar
    validacion = validar_guia(guia_final)

    # Paso 7: si no es válida, informar los faltantes sin guardar
    if not validacion["valida"]:
        return {"ok": False, "faltantes": validacion["faltantes"]}

    # Paso 8: si es válida, guardar y devolver ok y ruta
    return guardar_markdown(_nombre_archivo(tema), guia_final)


def main():
    tema = input("Tema de Python: ").strip()
    if not tema:
        print("El tema no puede estar vacío.")
        return 1

    resultado = ejecutar_flujo(tema)

    if resultado["ok"]:
        print(f"Guía guardada en: {resultado['ruta']}")
        return 0

    if "faltantes" in resultado:
        print("La guía no es válida. Faltan: " + ", ".join(resultado["faltantes"]))
    else:
        print(f"No se pudo guardar la guía: {resultado['error']}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
