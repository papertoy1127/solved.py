from ..solved_types import JObject, Repr, Uri
from typing import cast, Optional

class BackgroundAuthor(Repr):
    def __init__(self, data: JObject):
        self.authorId = cast(str, data["authorId"])
        self.role = cast(str, data["role"])
        self.authorUrl = cast(Optional[Uri], data["authorUrl"])
        self.handle = cast(Optional[str], data["handle"])
        self.twitter = cast(Optional[str], data["twitter"])
        self.instagram = cast(Optional[str], data["instagram"])
        self.displayName = cast(str, data["displayName"])