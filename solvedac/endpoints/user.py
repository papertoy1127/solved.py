from ..schemes import Organization as _Organization, User as _User, ProblemStats as _ProblemStats
from ..schemes import Problem as _Problem, ClassStats as _ClassStats, TagStats as _TagStats, CountedArray as _CountedArray
from ..session import SolvedSession as _SolvedSession
from typing import Sequence as _Sequence, Optional as _Optional
import json

async def organizations(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_Sequence[_Organization]]:
    resp = await session.get("https://solved.ac/api/v3/user/_Organizations", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _Organization(x), json.loads(await resp.text())))

    if resp.status == 404:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def show(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_User]:
    resp = await session.get("https://solved.ac/api/v3/user/show", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return _User(json.loads(await resp.text()));

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def problem_stats(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_ProblemStats]:
    resp = await session.get("https://solved.ac/api/v3/user/problem_stats", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return _ProblemStats(json.loads(await resp.text()));

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def top_100(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_CountedArray[_Problem]]:
    resp = await session.get("https://solved.ac/api/v3/user/top_100", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        dat = json.loads(await resp.text())
        return _CountedArray(dat["count"], list(map(lambda x: _Problem(x), dat["items"])))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")


async def class_stats(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_Sequence[_ClassStats]]:
    resp = await session.get("https://solved.ac/api/v3/user/class_stats", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _ClassStats(x), json.loads(await resp.text())))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")


async def tag_stats(session: _SolvedSession, handle: str, page: int, **kwargs) -> _Optional[_CountedArray[_TagStats]]:
    resp = await session.get("https://solved.ac/api/v3/user/problem_tag_stats", {
        "handle": handle,
        "page": page,
        **kwargs,
    })

    if resp.status == 200:
        dat = json.loads(await resp.text())
        return _CountedArray(dat["count"], list(map(lambda x: _TagStats(x), dat["items"])))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")