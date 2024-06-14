from ...solved_types import JObject, Repr
from typing import cast

class ProblemTagNameTranslated(Repr):
    def __init__(self, data: JObject):
        self.language = cast(str, data["language"])
        self.name = cast(str, data["name"])
        self.short = cast(str, data["short"])