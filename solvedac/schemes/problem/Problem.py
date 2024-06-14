from ...solved_types import JObject, JArray, Repr
from typing import cast, Sequence
from .ProblemLevel import ProblemLevel
from .ProblemTitleTranslated import ProblemTitleTranslated
from .ProblemTag import ProblemTag

class Problem(Repr):
    def __init__(self, data: JObject):
        self.problemId = cast(int, data["problemId"])
        self.titleKo = cast(str, data["titleKo"])
        
        self.titles: Sequence[ProblemTitleTranslated] = \
            list(map(lambda x: ProblemTitleTranslated(cast(JObject, x)), cast(JArray, data["titles"])))
        
        self.isSolvable = cast(bool, data["isSolvable"])
        self.isPartial = cast(bool, data["isPartial"])
        self.acceptedUserCount = cast(int, data["acceptedUserCount"])
        self.level = ProblemLevel(cast(int, data["level"]))
        self.votedUserCount = cast(int, data["votedUserCount"])
        self.sprout = cast(bool, data["sprout"])
        self.givesNoRating = cast(bool, data["givesNoRating"])
        self.isLevelLocked = cast(bool, data["isLevelLocked"])
        self.averageTries = cast(float, data["averageTries"])
        self.official = cast(bool, data["official"])
        
        self.tags: Sequence[ProblemTag] = \
            list(map(lambda x: ProblemTag(cast(JObject, x)), cast(JArray, data["tags"])))
        
        self.metadata = data["metadata"]