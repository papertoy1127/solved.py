from datetime import datetime, date
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T', bound=datetime|date)
U = TypeVar('U')

@dataclass
class History(Generic[T,U]):
    timestamp: T
    value: U

    def __str__(self):
        return f"<{str(self.timestamp)}; {self.value}>"

    def __repr__(self):
        return str(self)