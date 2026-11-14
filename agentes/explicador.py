"""Agente explicador. Completa este archivo en la tarea correspondiente."""

import os

from google.adk.agents import Agent


def crear_agente_explicador():
    """Crea el agente que explica un tema de Python."""
    modelo = os.getenv("GEMINI_MODEL")

    return Agent(
        name="explicador_python",
        model=modelo,
        description="Explica temas de Python a principiantes con un ejemplo y un error frecuente.",
        instruction=(
            "Eres un asistente que enseña Python a principiantes. "
            "Responde siempre en español. "
            "Explica de forma breve el tema que recibas: qué es y para qué sirve. "
            "Incluye un único ejemplo pequeño en un bloque de código marcado como python. "
            "Menciona un error frecuente relacionado con el tema y cómo evitarlo. "
            "No agregues temas que no se pidieron ni inventes comportamientos del lenguaje."
        ),
    )
