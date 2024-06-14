from enum import Enum

class BadgeTier(str, Enum):
    def __str__(self):
        return self.value
    
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    MASTER = "master"