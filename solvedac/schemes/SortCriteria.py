from enum import Enum

class SortCriteria(str, Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.name.upper()}>"
    
    ID = "id"
    LEVEL = "level"
    TITLE = "title"
    SOLVED = "solved"
    AVERAGE_TRY = "average_try"
    RANDOM = "random"