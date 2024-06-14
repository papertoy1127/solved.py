from .AutoComplete import AutoComplete
from ...solved_types import JObject
from typing import cast

class BriefProblem(AutoComplete):   
    def __init__(self, data: JObject):
        self.id = cast(int, data["id"])
        self.title = cast(str, data["title"])
        self.solved = cast(int, data["solved"])
        super().__init__(data)