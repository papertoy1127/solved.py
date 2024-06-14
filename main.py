from solvedac.session import SolvedSession
from solvedac.endpoints import *
from solvedac.schemes import *
import asyncio

async def main():
    session = SolvedSession("ko")
    a = await search.tag(session, "number_theory", 1)
    print(a)
    a = await search.tag(session, "a n", 2)
    print(a)

if __name__ == "__main__":
    asyncio.run(main())