from .History import History
from .GrassTheme import GrassTheme
from .GrassTopic import GrassTopic
from ..solved_types import JObject, JArray, Repr
from typing import Any, Sequence, cast, Literal
from datetime import datetime

class Grass(Repr):
    def __init__(self, data: JObject):
        self.grass: Sequence[History[int|Literal['frozen','repaired-incremented']]] = list(map(lambda x: History(datetime.strptime(x["date"], "%Y-%m-%d").date(), x["value"]), cast(Sequence[Any], data["grass"])))
        self.theme = cast(str, data["theme"])
        self.currentStreak = cast(int, data["currentStreak"])
        self.longestStreak = cast(int, data["longestStreak"])
        self.topic = GrassTopic(cast(int, data["topic"]))