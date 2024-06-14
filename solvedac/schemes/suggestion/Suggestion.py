from ...solved_types import JObject, JArray, Repr
from .AutoComplete import AutoComplete
from .BriefProblem import BriefProblem
from .BriefProblemTag import BriefProblemTag
from ..user.User import User
from typing import cast, Sequence

class Suggestion(Repr):
    def __init__(self, data: JObject):
        self.autocomplete: Sequence[AutoComplete] = \
            list(map(lambda x: AutoComplete(cast(JObject, x)), cast(JArray, data["autocomplete"])))
        
        self.problems: Sequence[BriefProblem] = \
            list(map(lambda x: BriefProblem(cast(JObject, x)), cast(JArray, data["problems"])))
        
        self.problemCount = cast(int, data["problemCount"])
        
        self.tags: Sequence[BriefProblemTag] = \
            list(map(lambda x: BriefProblemTag(cast(JObject, x)), cast(JArray, data["tags"])))
        
        self.tagCount = cast(int, data["tagCount"])
        
        self.users: Sequence[User] = \
            list(map(lambda x: User(cast(JObject, x)), cast(JArray, data["users"])))
        
        self.userCount = cast(int, data["userCount"])