from ..solved_types import JObject, Repr, ClassNum
from typing import cast

class ClassInfo(Repr):
    def __init__(self, data: JObject):
        self.classNum = cast(ClassNum, data["class"])
        self.total = cast(int, data["total"])
        self.essentials = cast(int, data["essentials"])
        self.criteria = cast(int, data["criteria"])