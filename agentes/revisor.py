"""Agente revisor."""

import os

from google.adk.agents import Agent


def crear_agente_revisor():
    """Crea el agente que entrega la guía Markdown revisada."""
    modelo = os.getenv("GEMINI_MODEL")

    return Agent(
        name="revisor_python",
        model=modelo,
        description="Revisa el borrador de una guía de Python y devuelve la guía final con una sección de revisión.",
        instruction=(
            "Eres un revisor de guías de estudio de Python para principiantes. "
            "Recibirás el borrador completo de una guía en Markdown. "
            "Comprueba que el tema, la explicación, el ejemplo y la práctica se correspondan y corrige los errores graves. "
            "Devuelve únicamente la guía final en Markdown, sin texto introductorio y sin encerrarla en un bloque de código. "
            "Conserva sin cambios el título y los encabezados '## Explicación' y '## Práctica'. "
            "Conserva los bloques de código marcados como python. "
            "Agrega al final una única sección '## Revisión' con una lista breve de las mejoras realizadas. "
            "Si no hubo mejoras, escribe en esa sección: No se requirieron cambios importantes. "
            "No inventes comportamientos de Python ni elimines secciones requeridas. "
            "Responde siempre en español."
        ),
    )
