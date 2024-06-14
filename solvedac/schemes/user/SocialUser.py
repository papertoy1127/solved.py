from ...solved_types import JObject, Repr
from typing import cast
from .User import User

class SocialUser(User):
    def __init__(self, data: JObject):
        super().__init__(data)
        self.blocked = cast(bool, data["blocked"])
        self.reverseBlocked = cast(bool, data["reverseBlocked"])
        self.isRival = cast(bool, data["isRival"])
        self.isReverseRival = cast(bool, data["isReverseRival"])