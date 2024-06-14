from typing import TypeVar, Generic, Sequence, NamedTuple

T = TypeVar('T')

class CountedArray(Generic[T]):
    def __init__(self, count: int, seq: Sequence[T]):
        self.count = count
        self.items = seq

    def __str__(self):
        return f"[{self.count}|{', '.join(map(lambda x: x.__repr__(), self.items))}]";

    def __repr__(self):
        return str(self)