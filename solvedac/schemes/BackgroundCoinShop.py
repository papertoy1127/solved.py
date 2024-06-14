from .Background import Background
from ..solved_types import JObject, Repr, Uri
from typing import cast, Literal

class BackgroundCoinShop(Repr):
    def __init__(self, data: JObject):
        self.background = Background(cast(JObject, data["background"]))
        self.priceUnit = cast(Literal["coins", "stardusts"], data["priceUnit"])
        self.price = cast(int, data["price"])