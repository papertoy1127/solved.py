from enum import Enum

class BadgeCategory(str, Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name.upper()}>"
    
    EVENT = "event"
    ACHIEVEMENT = "achievement"
    SEASON = "season"
    CONTEST = "contest"