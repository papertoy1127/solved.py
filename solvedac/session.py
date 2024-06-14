from aiohttp import ClientSession, ClientResponse
from typing import Mapping, Any

class SolvedSession:
    def __init__(self, lang: str):
        self.lang = lang

    async def get(self, url: str, params: Mapping[str, Any]|None = None) -> ClientResponse:
        d: dict[str, object] = { } if params is None else { **params }
        for k, v in list(d.items()):
            if v is None:
                d.pop(k)
        
        print(d)

        async with ClientSession(headers={"x-solvedac-language": self.lang,}) as session:
            return await session.get(url, params=d)