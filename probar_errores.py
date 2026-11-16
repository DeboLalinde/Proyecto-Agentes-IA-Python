"""Pruebas manuales de la Tarea 8: errores simulados sin usar la API."""

import os
import tempfile
from pathlib import Path

import main
from herramientas.archivos import guardar_markdown
from runtime.errores import (
    ConfiguracionIncompleta,
    LimiteTemporal,
    RespuestaVacia,
    ServicioNoDisponible,
)

os.environ["GEMINI_MODEL"] = "modelo-local-para-pruebas"
os.chdir(tempfile.mkdtemp())


def lanzar(error):
    def ejecutar(agente, mensaje):
        raise error
    return ejecutar


def devolver(texto):
    def ejecutar(agente, mensaje):
        return texto
    return ejecutar


def probar(nombre, ejecutar, tema="listas"):
    invocaciones = []

    def contador(agente, mensaje):
        invocaciones.append(agente.name)
        return ejecutar(agente, mensaje)

    try:
        resultado = main.ejecutar_flujo(tema, ejecutar=contador)
        print(f"{nombre}: {resultado} | invocaciones: {len(invocaciones)}")
    except (ValueError, ConfiguracionIncompleta, LimiteTemporal,
            ServicioNoDisponible, RespuestaVacia) as error:
        print(f"{nombre}: {type(error).__name__}: {error} | invocaciones: {len(invocaciones)}")


probar("Tema vacío", devolver("no usado"), tema="   ")
probar("Falta configuración", lanzar(ConfiguracionIncompleta("Falta configurar: GOOGLE_API_KEY.")))
probar("Cuota", lanzar(LimiteTemporal("Se alcanzó un límite de cuota.")))
probar("Servicio", lanzar(ServicioNoDisponible("El servicio no está disponible.")))
probar("Respuesta vacía", devolver(""))
probar("Guía inválida", devolver("texto sin estructura"))

# Fallo de escritura simulado
escritura_original = Path.write_text


def escritura_rota(self, *args, **kwargs):
    raise OSError("disco lleno (simulado)")


Path.write_text = escritura_rota
resultado = guardar_markdown("guia_prueba.md", "contenido")
Path.write_text = escritura_original
restos = [p.name for p in Path("salida").glob("*")] if Path("salida").exists() else []
print(f"Fallo de escritura: {resultado} | archivos en salida: {restos}")
