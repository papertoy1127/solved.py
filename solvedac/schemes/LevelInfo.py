from .problem import ProblemLevel
from ..solved_types import JObject, Repr
from typing import cast

class LevelInfo(Repr):
    def __init__(self, data: JObject):
        self.level = cast(ProblemLevel, data["level"])
        self.count = cast(int, data["count"])