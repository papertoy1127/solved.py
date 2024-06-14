from datetime import datetime, date
from dataclasses import dataclass

@dataclass
class History:
    timestamp: datetime|date
    value: int

    def __str__(self):
        return f"<{str(self.timestamp)}; {self.value}>"

    def __repr__(self):
        return str(self)