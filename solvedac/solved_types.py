from typing import Mapping as _Mapping, Sequence as _Sequence, Literal as _Literal, NewType as _NewType

JObject = _Mapping[str, "JSON"];
JArray = _Sequence["JSON"];
JSON = JObject | JArray | str | int | float | bool | None

ClassNum = _Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Uri = _NewType('Uri', str)

class Repr():
    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return str(vars(self))