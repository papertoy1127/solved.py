from ..solved_types import JObject, JArray, Uri, Repr
from typing import cast, Optional, Sequence
from .BackgroundCategory import BackgroundCategory
from .BackgroundAuthor import BackgroundAuthor

class Background(Repr):
    def __init__(self, data: JObject):
        self.backgroundId = cast(str, data["backgroundId"])
        self.backgroundImageUrl = cast(Uri, data["backgroundImageUrl"])
        self.fallbackBackgroundImageUrl = cast(Optional[Uri], data["fallbackBackgroundImageUrl"])
        self.backgroundVideoUrl = cast(Optional[Uri], data["backgroundVideoUrl"])
        self.unlockedUserCount = cast(int, data["unlockedUserCount"])
        self.displayName = cast(str, data["displayName"])
        self.displayDescription = cast(str, data["displayDescription"])
        self.conditions = cast(Optional[str], data["conditions"])
        self.hiddenConditions = cast(bool, data["hiddenConditions"])
        self.isIllust = cast(bool, data["isIllust"])
        self.backgroundCategory = BackgroundCategory(cast(str, data["backgroundCategory"]))
        self.solvedCompanyRights = cast(bool, data["solvedCompanyRights"])
        
        self.authors: Sequence[BackgroundAuthor] = \
            list(map(lambda x: BackgroundAuthor(cast(JObject, x)), cast(JArray, data["authors"])))