from dataclasses import dataclass

from sicm_core.config.enums import ShockType


@dataclass(slots=True)
class Shock:

    type: ShockType

    magnitude: float

    description: str = ""
