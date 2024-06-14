from enum import Enum

class BackgroundCategory(str, Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.name.upper()}>"
    
    EVENT = "event"
    ARENA = "arena"
    ACHIEVEMENT = "achievement"
    SEASON = "season"
    CONTEST = "contest"