from ..schemes import Problem as _Problem, SortCriteria as _SortCriteria, CountedArray as _CountedArray
from ..schemes import ProblemTag as _ProblemTag
from ..session import SolvedSession as _SolvedSession
from typing import Sequence as _Sequence, Literal as _Literal
import json

async def problem(session: _SolvedSession, query: str, page: int, *, direction: _Literal["asc", "desc"]|None = None, sort: _SortCriteria|None = None, **kwargs) -> _CountedArray[_Problem]:
    resp = await session.get("https://solved.ac/api/v3/search/problem", {
        "query": query,
        "direction": direction,
        "page": page,
        **kwargs,
    })

    if resp.status == 200:
        dat = json.loads(await resp.text())
        return _CountedArray(dat["count"], list(map(lambda x: _Problem(x), dat["items"])))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def tag(session: _SolvedSession, query: str, page: int, **kwargs) -> _CountedArray[_ProblemTag]:
    resp = await session.get("https://solved.ac/api/v3/search/tag", {
        "query": query,
        "page": page,
        **kwargs,
    })

    if resp.status == 200:
        dat = json.loads(await resp.text())
        return _CountedArray(dat["count"], list(map(lambda x: _ProblemTag(x), dat["items"])))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")