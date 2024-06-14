from ..solved_types import JObject, Repr, Uri
from typing import cast

class Item(Repr):
    def __init__(self, data: JObject):
        self.itemId = cast(str, data["itemId"])
        self.itemImageUrl = cast(Uri, data["itemImageUrl"])
        self.inventoryMaxUnits = cast(int, data["inventoryMaxUnits"])
        self.usable = cast(bool, data["inventoryMaxUusablenits"])
        self.displayName = cast(str, data["displayName"])
        self.displayDescription = cast(str, data["displayDescription"])