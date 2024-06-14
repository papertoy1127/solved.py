from ...solved_types import JObject, Repr
from typing import cast
from ..problem.ProblemTag import ProblemTag

class TagRating(Repr):
    def __init__(self, data: JObject):
        self.tag = ProblemTag(cast(JObject, data["tag"]))
        self.solvedCount = cast(int, data["solvedCount"])
        self.rating = cast(int, data["rating"])
        self.ratingByProblemsSum = cast(int, data["ratingByProblemsSum"])
        self.ratingByClass = cast(int, data["ratingByClass"])
        self.ratingBySolvedCount = cast(int, data["ratingBySolvedCount"])
        self.ratingProblemsCutoff = cast(int, data["ratingProblemsCutoff"])