from datetime import datetime, date
from typing import NamedTuple

class History(NamedTuple):
    timestamp: datetime|date
    value: int

    def __str__(self):
        return f"<{str(self.timestamp)}; {self.value}>"

    def __repr__(self):
        return str(self)