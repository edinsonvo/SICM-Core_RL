from dataclasses import dataclass

from uuid import UUID

from sicm_core.domain.metadata import Metadata

from sicm_core.domain.scenario import Scenario


@dataclass(slots=True)
class Experiment:

    id: UUID

    name: str

    scenario: Scenario

    metadata: Metadata
