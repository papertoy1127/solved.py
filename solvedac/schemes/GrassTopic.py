from enum import Enum

class GrassTopic(str, Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name.upper()}>"
    
    TODAY_SOLVED = "today_solved"
    TODAY_SOLVED_MAX_TIER = "today-solved-max-tier"