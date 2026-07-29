@dataclass(slots=True)

class ExecutionResult:

    equilibrium: Equilibrium

    iterations: int

    execution_time: float

    converged: bool
