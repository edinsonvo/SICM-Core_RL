from dataclasses import dataclass


@dataclass(slots=True)
class EconomyParameters:

    C0: float = 50

    c: float = .8

    I0: float = 100

    b: float = 5

    G: float = 150

    T: float = 120

    M: float = 500

    P: float = 1

    k: float = .5

    h: float = 10

    NX0: float = 20

    A: float = 1

    K: float = 100

    alpha: float = .33
