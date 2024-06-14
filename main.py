from solvedac.session import SolvedSession
from solvedac.endpoints import *
from solvedac.schemes import *
import asyncio

async def main():
    session = SolvedSession("ko")
    a = await user.grass(session, "cywohoy", GrassTopic.TODAY_SOLVED_MAX_TIER)
    print(a)

if __name__ == "__main__":
    asyncio.run(main())