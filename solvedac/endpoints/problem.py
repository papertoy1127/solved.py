from ..schemes import ClassInfo as _ClassInfo, LevelInfo as _LevelInfo, Problem as _Problem
from ..schemes import SproutInfo as _SproutInfo
from ..session import SolvedSession as _SolvedSession
from typing import Sequence as _Sequence, Optional as _Optional
import json

async def clazz(session: _SolvedSession, **kwargs) -> _Sequence[_ClassInfo]:
    resp = await session.get("https://solved.ac/api/v3/problem/class", { **kwargs })

    if resp.status == 200:
        return list(map(lambda x: _ClassInfo(x), json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def level(session: _SolvedSession, **kwargs) -> _Sequence[_LevelInfo]:
    resp = await session.get("https://solved.ac/api/v3/problem/level", { **kwargs })

    if resp.status == 200:
        return list(map(lambda x: _LevelInfo(x), json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def lookup(session: _SolvedSession, *problems, **kwargs) -> _Sequence[_Problem]:
    resp = await session.get("https://solved.ac/api/v3/problem/lookup", {
        "problemIds": ','.join(map(str, problems)),
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _Problem(x), json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def show(session: _SolvedSession, problemId: int, **kwargs) -> _Optional[_Problem]:
    resp = await session.get("https://solved.ac/api/v3/problem/show", {
        "problemId": problemId,
        **kwargs,
    })

    if resp.status == 200:
        return _Problem(json.loads(await resp.text()))
    
    if resp.status == 404:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def sprout_lookup(session: _SolvedSession, **kwargs) -> _Sequence[_SproutInfo]:

    resp = await session.get("https://solved.ac/api/v3/problem/sprout_lookup", {
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _SproutInfo(x), json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")