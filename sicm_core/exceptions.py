"""
Excepciones del proyecto.
"""


class SICMError(Exception):
    """Clase base de excepciones."""


class ModelNotFoundError(SICMError):
    """Modelo económico no registrado."""


class InvalidScenarioError(SICMError):
    """Escenario inválido."""


class SolverError(SICMError):
    """Error durante la resolución."""
