import re, sys
_color_pattern = re.compile(r'\#([0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F])([0-9a-fA-F][0-9a-fA-F])')

class Color:
    def __init__(self, color: str):
        m = _color_pattern.match(color)
        if (m is None) or (m.span() != (0, len(color))):
            sys.stderr.write(f"Failed to parse color: {color}\n")
            self.r = 0
            self.g = 0
            self.b = 0

            self.htmlFormat: str = "#000000"

        else:
            self.r = int(m.group(1), 16)
            self.g = int(m.group(2), 16)
            self.b = int(m.group(3), 16)

            self.htmlFormat: str = color.upper()
    
    def __str__(self):
        return self.htmlFormat
    
    def __repr__(self):
        return self.htmlFormat