from enum import Enum

class ClassDecoration(str, Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name.upper()}>"
    
    NONE = "none"
    SILVER = "silver"
    GOLD = "gold"