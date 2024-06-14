from ...solved_types import JObject, Repr, ClassNum
from typing import cast
from typing import Optional, Literal
from .SolveTier import SolveTier
from .ArenaTier import ArenaTier
from datetime import datetime

class User(Repr):
    def __init__(self, data: JObject):
        self.handle = cast(str, data["handle"])
        self.bio = cast(str, data["bio"])
        self.badgeId = cast(Optional[str], data["badgeId"])
        self.backgroundId = cast(str, data["backgroundId"])
        self.profileImageUrl = cast(Optional[str], data["profileImageUrl"])
        self.solvedCount = cast(int, data["solvedCount"])
        self.voteCount = cast(int, data["voteCount"])
        self.classNum = cast(ClassNum, data["class"])
        self.classDecoration = cast(Literal['none', 'silver', 'gold'], data["classDecoration"])
        self.rivalCount = cast(int, data["rivalCount"])
        self.reverseRivalCount = cast(int, data["reverseRivalCount"])
        self.tier = SolveTier(cast(int, data["tier"]))
        self.rating = cast(int, data["rating"])
        self.ratingByProblemsSum = cast(int, data["ratingByProblemsSum"])
        self.ratingByClass = cast(int, data["ratingByClass"])
        self.ratingBySolvedCount = cast(int, data["ratingBySolvedCount"])
        self.ratingByVoteCount = cast(int, data["ratingByVoteCount"])
        self.arenaTier = ArenaTier(cast(int, data["arenaTier"]))
        self.arenaRating = cast(int, data["arenaRating"])
        self.arenaMaxTier = ArenaTier(cast(int, data["arenaMaxTier"]))
        self.arenaMaxRating = cast(int, data["arenaMaxRating"])
        self.arenaCompetedRoundCount = cast(int, data["arenaCompetedRoundCount"])
        self.maxStreak = cast(int, data["maxStreak"])
        self.coins = cast(int, data["coins"])
        self.stardusts = cast(int, data["stardusts"])
        self.joinedAt = datetime.strptime(cast(str, data["joinedAt"]), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.bannedUntil = datetime.strptime(cast(str, data["bannedUntil"]), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.proUntil = datetime.strptime(cast(str, data["proUntil"]), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.rank = cast(int, data["rank"])