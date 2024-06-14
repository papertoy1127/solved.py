from ...solved_types import JObject, Repr, ClassNum
from typing import Optional, cast
from .Gender import Gender

class AdditionalInfo(Repr):
    def __init__(self, data: JObject):
        self.countryCode = cast(Optional[str], data["countryCode"])
        self.gender = Gender(cast(str, data["gender"]))
        self.pronouns = cast(Optional[str], data["pronouns"])
        self.birthYear = cast(Optional[str], data["birthYear"])
        self.birthMonth = cast(Optional[str], data["birthMonth"])
        self.birthDay = cast(Optional[str], data["birthDay"])
        self.name = cast(Optional[str], data["name"])
        self.nameNative = cast(Optional[str], data["nameNative"])