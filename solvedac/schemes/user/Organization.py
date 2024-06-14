from ...solved_types import JObject, Repr
from typing import cast
from .OrganizationType import OrganizationType
from ..Color import Color

class Organization(Repr):
    def __init__(self, data: JObject):
        self.organizationId = cast(str, data["organizationId"])
        self.name = cast(str, data["name"])
        self.type = OrganizationType(cast(str, data["type"]))
        self.rating = cast(str, data["rating"])
        self.userCount = cast(str, data["userCount"])
        self.voteCount = cast(str, data["voteCount"])
        self.solvedCount = cast(str, data["solvedCount"])
        self.color = Color(cast(str, data["color"]))