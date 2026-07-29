from dataclasses import dataclass


@dataclass(slots=True)
class Metrics:

    iterations: int

    execution_time: float

    converged: bool
