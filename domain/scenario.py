from dataclasses import dataclass

from sicm_core.domain.parameters import EconomyParameters

from sicm_core.domain.shock import Shock

from sicm_core.config.enums import ModelType


@dataclass(slots=True)
class Scenario:

    model: ModelType

    parameters: EconomyParameters

    shocks: list[Shock]
