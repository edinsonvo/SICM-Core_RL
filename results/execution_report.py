@dataclass(slots=True)

class ExecutionReport:

    experiment: Experiment

    result: ExecutionResult

    interpretation: str

    warnings: list[str]

    errors: list[str]
