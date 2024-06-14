from ..schemes import Organization as _Organization, User as _User, ProblemStats as _ProblemStats
from ..schemes import Problem as _Problem, ClassStats as _ClassStats, TagStats as _TagStats, TagRating as _TagRating
from ..schemes import CountedArray as _CountedArray, Badge as _Badge, AdditionalInfo as _AdditionalInfo
from ..schemes import History as _History, Grass as _Grass, GrassTopic as _GrassTopic
from ..session import SolvedSession as _SolvedSession
from typing import cast as _cast, Sequence as _Sequence, Optional as _Optional, Literal as _Literal
from ..solved_types import JObject as _JObject
from datetime import datetime as _datetime
import json

async def organizations(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_Sequence[_Organization]]:
    resp = await session.get("https://solved.ac/_JObjectrganizations", {
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

async def tag_ratings(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_Sequence[_TagRating]]:
    resp = await session.get("https://solved.ac/api/v3/user/tag_ratings", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _TagRating(x), json.loads(await resp.text())))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")


async def badge_stand(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_Sequence[_Badge]]:
    resp = await session.get("https://solved.ac/api/v3/user/badge_stand", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _Badge(x), json.loads(await resp.text())))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def additional_info(session: _SolvedSession, handle: str, **kwargs) -> _Optional[_AdditionalInfo]:
    resp = await session.get("https://solved.ac/api/v3/user/additional_info", {
        "handle": handle,
        **kwargs,
    })

    if resp.status == 200:
        return _AdditionalInfo(_cast(_JObject, json.loads(await resp.text())))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def histroy(session: _SolvedSession, handle: str, topic: _Literal["rating", "ratingRank", "solvedCount", "voteCount"], **kwargs) -> _Optional[_Sequence[_History[int]]]:
    resp = await session.get("https://solved.ac/api/v3/user/history", {
        "handle": handle,
        "topic": topic,
        **kwargs,
    })

    if resp.status == 200:
        return list(map(lambda x: _History(_datetime.strptime(_cast(str, x["timestamp"]), "%Y-%m-%dT%H:%M:%S.%fZ"), _cast(int, x["value"])), json.loads(await resp.text())))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")

async def grass(session: _SolvedSession, handle: str, topic: _Optional[_GrassTopic] = None, **kwargs) -> _Optional[_Grass]:
    if topic is None:
        topic_str: str = 'default'
    else:
        topic_str: str = topic.value

    resp = await session.get("https://solved.ac/api/v3/user/grass", {
        "handle": handle,
        "topic": topic_str,
        **kwargs,
    })

    if resp.status == 200:
        return _Grass(_cast(_JObject, json.loads(await resp.text())))

    if resp.status == 400:
        return None
    
    raise Exception(f"Failed to request GET from {resp.url} with error code {resp.status}")