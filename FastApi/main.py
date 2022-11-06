import uvicorn
from pydantic import conlist
from fastapi import FastAPI, Query, Path
from fastapi.responses import HTMLResponse

import pokemon_info
from model import PokeInfo
from client_session import request_client

app = FastAPI(
    title="Poke Info API",
    version="1.0.0",
    description=open("Readme.md").read(),
    docs_url="/swagger"
)

@app.get(
    "/rapidoc",
    response_class=HTMLResponse,
    include_in_schema=False
)
async def rapidoc():
    return f"""
        <!doctype html> <!-- Important: must specify -->
        <html>
            <head>
                <meta charset="utf-8"> <!-- Important: rapi-doc uses utf8 characters -->
                <script type="module" src="https://unpkg.com/rapidoc/dist/rapidoc-min.js"></script>
            </head>
            <body>
                <rapi-doc spec-url = "{app.openapi_url}"> </rapi-doc>
            </body>
        </html>
    """

@app.get(
    "/pokemon",
    description="Get Pokemons' infos given offset and limit",
    response_model=list[PokeInfo],
    response_description="Pokemon Infos"
)
async def poke_infos_from_offset_limits(
    offset: int = Query(
        ...,
        description="The offset of the pokemon to retrieval",
        ge=0,
        le=100
    ),
    limit: int = Query(
        ...,
        description="The limit of the pokemon to retrieval",
        ge=0,
        le=10
    ),
) -> list[PokeInfo]:
    poke_infos = await pokemon_info.get_pokeinfos_from_offset_limit(offset, limit)
    return poke_infos


@app.get(
    "/pokemon/ids",
    description="Get Pokemons' infos given their ids",
    response_model=list[PokeInfo],
    response_description="Pokemon Infos"
)
async def poke_infos_from_ids(
    poke_ids: conlist(
        int,
        min_items=1,
        max_items=10,
        unique_items=True
        ) = Query(
        ...,
        description="The ids of the pokemons for retrieval",
    )
) -> list[PokeInfo]:
    poke_infos = await pokemon_info.get_pokeinfos_from_ids(poke_ids)
    return poke_infos


@app.get(
    "/pokemon/names",
    description="Get Pokemons' infos given their names",
    response_model=list[PokeInfo],
    response_description="Pokemon Infos"
)
async def poke_infos_from_names(
    names: conlist(
        str,
        min_items=1,
        max_items=10,
        unique_items=True
        ) = Query(
        ...,
        description="The names of the pokemons for retrieval"
    )
) -> list[PokeInfo]:
    poke_infos = await pokemon_info.get_pokeinfos_from_names(names)
    return poke_infos


@app.get(
    "/pokemon/id/{poke_id}",
    description="Get a Pokemon's info given its id",
    response_model=PokeInfo,
    response_description="Pokemon Info"
)
async def poke_info_from_id(
    poke_id: int = Path(
        ...,
        description="The id of the pokemon to retrieve",
        ge=1,
        le=100
    )
) -> PokeInfo:
    poke_info = await pokemon_info.get_pokeinfo_from_id(poke_id)
    return poke_info

@app.get(
    "/pokemon/name/{name}",
    description="Get a Pokemon's info given its name",
    response_model=PokeInfo,
    response_description="Pokemon Info"
)
async def poke_info_from_name(
    name: str = Path(
        ...,
        description="The name of the pokemon to retrieve"
    )
) -> PokeInfo:
    poke_info = await pokemon_info.get_pokeinfo_from_name(name)
    return poke_info


app.on_event("startup")(request_client.__ainit__)
app.on_event("shutdown")(request_client.__adel__)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, use_colors=False)
