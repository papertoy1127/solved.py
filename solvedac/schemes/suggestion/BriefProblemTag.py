from .AutoComplete import AutoComplete
from ...solved_types import JObject
from typing import cast

class BriefProblemTag(AutoComplete):   
    def __init__(self, data: JObject):
        self.key = cast(str, data["key"])
        self.name = cast(str, data["name"])
        self.problemCount = cast(int, data["problemCount"])
        super().__init__(data)