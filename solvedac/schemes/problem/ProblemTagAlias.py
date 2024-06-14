from ...solved_types import JObject, Repr
from typing import cast

class ProblemTagAlias(Repr):
    def __init__(self, data: JObject):
        self.alias = cast(str, data["alias"])