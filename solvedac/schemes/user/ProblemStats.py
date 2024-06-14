from ...solved_types import JObject, Repr
from typing import cast
from ..problem.ProblemLevel import ProblemLevel

class ProblemStats(Repr):
    def __init__(self, data: JObject):
        self.level = ProblemLevel(cast(int, data["level"]))
        self.total = cast(int, data["total"])
        self.solved = cast(int, data["solved"])
        self.partial = cast(int, data["partial"])
        self.tried = cast(int, data["tried"])