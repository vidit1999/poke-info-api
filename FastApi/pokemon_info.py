import asyncio

from model import PokeInfo
from client_session import request_client

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def pokeresp_to_info(resp: dict) -> PokeInfo:
    return PokeInfo(
        poke_id=resp["id"],
        name=resp["name"],
        abilities=[
            ability_info.get("ability", {}).get("name")
            for ability_info in resp["abilities"]
        ],
        types=[
            type_info.get("type", {}).get("name")
            for type_info in resp["types"]
        ],
    )


def get_poke_id_from_url(url: str) -> int:
    return int(url.split("/")[-2])


async def get_pokeinfo_from_id(poke_id: int) -> PokeInfo:
    response = await request_client.client.get(f"{BASE_URL}/{poke_id}")
    return pokeresp_to_info(response.json())


async def get_pokeinfo_from_name(name: str) -> PokeInfo:
    response = await request_client.client.get(f"{BASE_URL}/{name}")
    return pokeresp_to_info(response.json())


async def get_pokeinfos_from_offset_limit(offset: int, limit: int) -> list[PokeInfo]:
    response = await request_client.client.get(
        f"{BASE_URL}",
        params={"offset": offset, "limit": limit}
    )
    resp = response.json()
    return await asyncio.gather(*[
        get_pokeinfo_from_id(get_poke_id_from_url(res["url"]))
        for res in resp["results"]
    ])


async def get_pokeinfos_from_ids(ids: list[int]) -> list[PokeInfo]:
    return await asyncio.gather(*[
        get_pokeinfo_from_id(poke_id)
        for poke_id in ids
    ])


async def get_pokeinfos_from_names(names: list[int]) -> list[PokeInfo]:
    return await asyncio.gather(*[
        get_pokeinfo_from_name(name)
        for name in names
    ])
