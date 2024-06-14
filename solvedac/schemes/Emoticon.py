from ..solved_types import JObject, Repr, Uri
from typing import cast

class Emoticon(Repr):
    def __init__(self, data: JObject):
        self.emoticonId = cast(str, data["emoticonId"])
        self.emoticonUrl = cast(Uri, data["emoticonUrl"])
        self.displayName = cast(str, data["displayName"])