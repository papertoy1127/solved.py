from ..schemes import Badge as _Badge
from ..session import SolvedSession as _SolvedSession
from typing import Optional as _Optional
import json

async def show(session: _SolvedSession, badgeId: str, **kwargs) -> _Optional[_Badge]:
    resp = await session.get("https://solved.ac/api/v3/badge/show", {
        "badgeId": badgeId,
        **kwargs,
    })

    if resp.status == 200:
        return _Badge(json.loads(await resp.text()));

    if resp.status == 404:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")
