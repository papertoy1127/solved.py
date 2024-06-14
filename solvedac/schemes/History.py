from datetime import datetime, date
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class History(Generic[T]):
    timestamp: datetime|date
    value: T

    def __str__(self):
        return f"<{str(self.timestamp)}; {self.value}>"

    def __repr__(self):
        return str(self)