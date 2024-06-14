from ..schemes import SiteStats as _SiteStats
from ..session import SolvedSession as _SolvedSession
import json

async def stats(session: _SolvedSession, **kwargs) -> _SiteStats:
    resp = await session.get("https://solved.ac/api/v3/site/stats", {
        **kwargs,
    })

    if resp.status == 200:
        return _SiteStats(json.loads(await resp.text()));
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")
