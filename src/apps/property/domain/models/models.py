from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Connection:
    cursor: Any


@dataclass
class ParamsProperty:
    year: Optional[int] = None
    city: Optional[str] = None
    state: Optional[str] = None
