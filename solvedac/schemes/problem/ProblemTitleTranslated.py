from ...solved_types import JObject, Repr
from typing import cast

class ProblemTitleTranslated(Repr):
    def __init__(self, data: JObject):
        self.language = cast(str, data["language"])
        self.languageDisplayName = cast(str, data["languageDisplayName"])
        self.title = cast(str, data["title"])
        self.isOriginal = cast(bool, data["isOriginal"])