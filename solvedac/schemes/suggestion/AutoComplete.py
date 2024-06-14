from ...solved_types import JObject, Repr
from typing import cast

class AutoComplete(Repr):   
    def __init__(self, data: JObject):
        self.caption = cast(str, data["caption"])
        self.description = cast(str, data["description"])