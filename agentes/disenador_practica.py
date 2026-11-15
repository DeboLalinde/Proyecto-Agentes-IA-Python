"""Agente diseñador de práctica."""

import os

from google.adk.agents import Agent


def crear_agente_disenador():
    """Crea el agente que propone una práctica sobre un tema de Python."""
    modelo = os.getenv("GEMINI_MODEL")

    return Agent(
        name="disenador_practica",
        model=modelo,
        description="Diseña un ejercicio de práctica de Python con criterios de aceptación y una pista.",
        instruction=(
            "Eres un asistente que diseña ejercicios de práctica de Python para principiantes. "
            "Recibirás un tema y una explicación previa; basa el ejercicio en esa explicación. "
            "Responde siempre en español. "
            "Propón un único ejercicio breve relacionado con el tema. "
            "Incluye exactamente tres criterios de aceptación observables en una lista. "
            "Agrega una pista que oriente sin revelar la solución completa. "
            "No repitas toda la explicación ni incluyas el código de la solución."
        ),
    )
