from ..schemes import CoinShopProduct as _CoinShopProduct, History as _History
from ..session import SolvedSession as _SolvedSession
from typing import Sequence as _Sequence, cast as _cast
from datetime import datetime as _datetime, date as _date
import json

async def exchange_rate(session: _SolvedSession, **kwargs) -> int:
    resp = await session.get("https://solved.ac/api/v3/coins/exchange_rate", {
        **kwargs,
    })

    if resp.status == 200:
        return int(await resp.text())

    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def exchange_rate_history(session: _SolvedSession, **kwargs) -> _Sequence[_History[_date,int]]:
    resp = await session.get("https://solved.ac/api/v3/coins/exchange_rate_history", {
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _History(_datetime.strptime(_cast(str, x["date"]), "%Y-%m-%d").date(), _cast(int, x["value"])), json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def shop_list(session: _SolvedSession, **kwargs) -> _Sequence[_CoinShopProduct]:
    resp = await session.get("https://solved.ac/api/v3/coins/shop/list", {
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _CoinShopProduct(x), json.loads(await resp.text())))
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")
