from ...solved_types import JObject, Repr
from typing import cast
from ..problem.ProblemTag import ProblemTag

class TagStats(Repr):
    def __init__(self, data: JObject):
        self.tag = ProblemTag(cast(JObject, data["tag"]))
        self.total = cast(int, data["total"])
        self.solved = cast(int, data["solved"])
        self.partial = cast(int, data["partial"])
        self.tried = cast(int, data["tried"])