from enum import Enum

class BadgeCategory(str, Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.name.upper()}>"
    
    EVENT = "event"
    ACHIEVEMENT = "achievement"
    SEASON = "season"
    CONTEST = "contest"