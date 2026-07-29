from enum import Enum


class ModelType(str, Enum):

    ISLM = "islm"

    MUNDELL_FLEMING = "mundell_fleming"

    CLASSICAL_CLOSED = "classical_closed"

    CLASSICAL_OPEN = "classical_open"


class ShockType(str, Enum):

    NONE = "none"

    FISCAL = "fiscal"

    MONETARY = "monetary"

    SUPPLY = "supply"

    EXTERNAL = "external"


class EconomyType(str, Enum):

    CLOSED = "closed"

    OPEN = "open"
