from enum import Enum

class GrassTheme(str, Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.name.upper()}>"
    
    COLOR_WINE = "color_wine"