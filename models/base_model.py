from abc import ABC
from abc import abstractmethod

from sicm_core.domain.experiment import Experiment
from sicm_core.results.execution_result import ExecutionResult


class BaseModel(ABC):

    name: str = ""

    family: str = ""

    version: str = "1.0"

    @abstractmethod
    def solve(
        self,
        experiment: Experiment
    ) -> ExecutionResult:
        """Resuelve el modelo."""
        raise NotImplementedError

    @abstractmethod
    def interpret(
        self,
        result: ExecutionResult
    ) -> str:
        """Genera interpretación económica."""
        raise NotImplementedError
