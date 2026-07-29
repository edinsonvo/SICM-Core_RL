@dataclass(slots=True)

class ExecutionContext:

    experiment: Experiment

    timestamp: datetime

    execution_id: UUID
