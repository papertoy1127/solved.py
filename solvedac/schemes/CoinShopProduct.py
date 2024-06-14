from ..solved_types import JObject, Repr
from typing import cast
from .Item import Item

class CoinShopProduct(Repr):
    def __init__(self, data: JObject):
        self.skuId = cast(str, data["skuId"])
        self.item = Item(cast(JObject, data["item"]))
        self.units = cast(int, data["units"])
        self.price = cast(int, data["price"])
        self.priceUnit = cast(str, data["priceUnit"])
        self.itemUseTimeLimited = cast(bool, data["itemUseTimeLimited"])
        self.itemSellTimeLimited = cast(bool, data["itemSellTimeLimited"])