from ...solved_types import JObject, Repr
from typing import cast
from .ClassDecoration import ClassDecoration

class ClassStats(Repr):
    def __init__(self, data: JObject):
        self.total = cast(int, data["total"])
        self.totalSolved = cast(int, data["totalSolved"])
        self.essentials = cast(int, data["essentials"])
        self.essentialSolved = cast(int, data["essentialSolved"])
        self.classNum = cast(int, data["class"])
        self.decoration = ClassDecoration(str(data["decoration"]).lower())