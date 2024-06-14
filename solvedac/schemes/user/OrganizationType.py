from enum import Enum

class OrganizationType(str, Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name.upper()}>"
    
    UNIVERSITY = "university"
    COMPANY = "company"
    COMMUNITY = "community"
    HIGH_SCHOOL = "high_school"
    MIDDLE_SCHOOL = "middle_school"
    ELEMENTARY_SCHOOL = "elementary_school"
    UNDEFINED = "undefined"