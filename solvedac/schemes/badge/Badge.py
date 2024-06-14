from ...solved_types import JObject, Repr, Uri
from typing import cast
from .BadgeCategory import BadgeCategory
from .BadgeTier import BadgeTier
from datetime import datetime

class Badge(Repr):
    def __init__(self, data: JObject):
        self.badgeId = cast(str, data["badgeId"])
        self.badgeImageUrl = cast(Uri, data["badgeImageUrl"])
        self.displayName = cast(str, data["displayName"])
        self.displayDescription = cast(str, data["displayDescription"])
        self.unlockedUserCount = cast(int, data["unlockedUserCount"])
        self.badgeTier = BadgeTier(cast(str, data["badgeTier"]))
        self.badgeCategory = BadgeCategory(cast(str, data["badgeCategory"]))
        self.solvedCompanyRights = cast(bool, data["solvedCompanyRights"])
        self.createdAt = datetime.strptime(cast(str, data["createdAt"]), "%Y-%m-%dT%H:%M:%S.%fZ")