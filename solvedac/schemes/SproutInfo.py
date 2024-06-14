from ..solved_types import JObject, JArray, Repr, ClassNum
from typing import cast
from .problem import Problem

class SproutInfo(Repr):
    def __init__(self, data: JObject):
        self.category = cast(str, data["category"])
        self.problemCount = cast(int, data["problemCount"])
        self.problems = list(map(lambda x: Problem(cast(JObject, x)), cast(JArray, data["problems"])))