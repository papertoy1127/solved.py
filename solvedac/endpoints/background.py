from ..schemes import Background as _Background, CountedArray as _CountedArray, BackgroundCoinShop as _BackgroundCoinShop
from ..session import SolvedSession as _SolvedSession
from typing import Optional as _Optional
import json

async def show(session: _SolvedSession, backgroundId: str, **kwargs) -> _Optional[_Background]:
    resp = await session.get("https://solved.ac/api/v3/background/show", {
        "backgroundId": backgroundId,
        **kwargs,
    })

    if resp.status == 200:
        return _Background(json.loads(await resp.text()));

    if resp.status == 404:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def shop_list(session: _SolvedSession, page: int, **kwargs) -> _CountedArray[_BackgroundCoinShop]:
    resp = await session.get("https://solved.ac/api/v3/background/shop/list", {
        "page": page,
        **kwargs,
    })

    if resp.status == 200:
        dat = json.loads(await resp.text())
        return _CountedArray(dat["count"], list(map(lambda x: _BackgroundCoinShop(x), dat["items"])))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")
