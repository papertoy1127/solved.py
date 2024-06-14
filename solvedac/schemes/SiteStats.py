from ..solved_types import JObject, Repr
from typing import cast

class SiteStats(Repr):
    def __init__(self, data: JObject):
        self.problemCount = cast(int, data["problemCount"])
        self.problemVotedCount = cast(int, data["problemVotedCount"])
        self.userCount = cast(int, data["userCount"])
        self.contributorCount = cast(int, data["contributorCount"])
        self.contributionCount = cast(int, data["contributionCount"])