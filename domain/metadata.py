from dataclasses import dataclass

from datetime import datetime


@dataclass(slots=True)
class Metadata:

    author: str

    institution: str

    created: datetime

    notes: str = ""
