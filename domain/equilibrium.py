from dataclasses import dataclass


@dataclass(slots=True)
class Equilibrium:

    Y: float

    r: float

    employment: float

    unemployment: float

    inflation: float

    exchange_rate: float
