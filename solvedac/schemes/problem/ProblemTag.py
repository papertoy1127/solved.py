from ...solved_types import JObject, JArray, Repr
from typing import cast, Sequence
from .ProblemTagAlias import ProblemTagAlias;
from .ProblemTagNameTranslated import ProblemTagNameTranslated;

class ProblemTag(Repr):
    def __init__(self, data: JObject):
        self.key = cast(str, data["key"])
        self.isMeta = cast(bool, data["isMeta"])
        self.bojTagId = cast(int, data["bojTagId"])
        self.problemCount = cast(int, data["problemCount"])
        
        self.displayNames: Sequence[ProblemTagNameTranslated] = \
            list(map(lambda x: ProblemTagNameTranslated(cast(JObject, x)), cast(JArray, data["displayNames"])))
        
        self.aliases: Sequence[ProblemTagAlias] = \
            list(map(lambda x: ProblemTagAlias(cast(JObject, x)), cast(JArray, data["aliases"])))