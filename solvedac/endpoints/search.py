from ..schemes import Problem as _Problem, SortCriteria as _SortCriteria, CountedArray as _CountedArray
from ..schemes import ProblemTag as _ProblemTag, User as _User, Suggestion as _Suggestion
from ..session import SolvedSession as _SolvedSession
from typing import Literal as _Literal, cast as _cast
from ..solved_types import JObject as _JObject
import json

async def problem(session: _SolvedSession, query: str, page: int, *, direction: _Literal["asc", "desc"]|None = None, sort: _SortCriteria|None = None, **kwargs) -> _CountedArray[_Problem]:
    resp = await session.get("https://solved.ac/api/v3/search/problem", {
        "query": query,
        "direction": direction,
        "page": page,
        "sort": sort,
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

async def user(session: _SolvedSession, query: str, page: int, **kwargs) -> _CountedArray[_User]:
    resp = await session.get("https://solved.ac/api/v3/search/user", {
        "query": query,
        "page": page,
        **kwargs,
    })

    if resp.status == 200:
        dat = json.loads(await resp.text())
        return _CountedArray(dat["count"], list(map(lambda x: _User(x), dat["items"])))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def suggestion(session: _SolvedSession, query: str, **kwargs) -> _Suggestion:
    resp = await session.get("https://solved.ac/api/v3/search/suggestion", {
        "query": query,
        **kwargs,
    })

    if resp.status == 200:
        return _Suggestion(_cast(_JObject, json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")