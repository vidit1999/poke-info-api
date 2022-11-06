from aiohttp import web

import pokemon_info

async def poke_info_from_id(request: web.Request, poke_id: int) -> web.Response:
    """
    ---
    summary: Get a Pokemon's info given its id
    parameters:
      - name: poke_id
        in: path
        required: true
        description: The id of the pokemon to retrieve
        schema:
          type: integer
          minimum: 1
          maximum: 100
    responses:
      '200':
        description: Pokemon Info
        content:
            application/json:
              schema:
                $ref: '#/components/schemas/PokeInfo'
    """
    poke_info = await pokemon_info.get_pokeinfo_from_id(poke_id)
    return web.json_response(data=poke_info.to_dict())


async def poke_info_from_name(request: web.Request, name: int) -> web.Response:
    """
    ---
    summary: Get a Pokemon's info given its name
    parameters:
      - name: name
        in: path
        required: true
        description: The name of the pokemon to retrieve
        schema:
          type: string
    responses:
      '200':
        description: Pokemon Info
        content:
            application/json:
              schema:
                $ref: '#/components/schemas/PokeInfo'
    """
    poke_info = await pokemon_info.get_pokeinfo_from_name(name)
    return web.json_response(data=poke_info.to_dict())


async def poke_infos_from_offset_limits(request: web.Request, offset: int, limit: int) -> web.Response:
    """
    ---
    summary: Get Pokemons' infos given offset and limit
    parameters:
      - in: query
        name: offset
        required: true
        description: The offset of the pokemon to retrieval
        schema:
          type: integer
          minimum: 0
          maximum: 100
      - in: query
        name: limit
        required: true
        description: The limit of the pokemon to retrieval
        schema:
          type: integer
          minimum: 1
          maximum: 10
    responses:
      '200':
        description: Pokemon Infos
        content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/PokeInfo"
    """
    poke_infos = await pokemon_info.get_pokeinfos_from_offset_limit(offset, limit)
    return web.json_response(data=list(map(lambda x: x.to_dict(), poke_infos)))


async def poke_infos_from_ids(request: web.Request, poke_ids: list[int]) -> web.Response:
    """
    ---
    summary: Get Pokemons' infos given their ids
    parameters:
      - in: query
        name: poke_ids
        required: true
        description: The ids of the pokemons for retrieval
        schema:
          type: array
          items:
            type: integer
          minItems: 1
          maxItems: 10
          uniqueItems: true
    responses:
      '200':
        description: Pokemon Infos
        content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/PokeInfo"
    """
    poke_infos = await pokemon_info.get_pokeinfos_from_ids(poke_ids)
    return web.json_response(data=list(map(lambda x: x.to_dict(), poke_infos)))


async def poke_infos_from_names(request: web.Request, names: list[str]) -> web.Response:
    """
    ---
    summary: Get Pokemons' infos given their names
    parameters:
      - in: query
        name: names
        required: true
        description: The names of the pokemons for retrieval
        schema:
          type: array
          items:
            type: string
          minItems: 1
          maxItems: 10
          uniqueItems: true
    responses:
      '200':
        description: Pokemon Infos
        content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/PokeInfo"
    """
    poke_infos = await pokemon_info.get_pokeinfos_from_names(names)
    return web.json_response(data=list(map(lambda x: x.to_dict(), poke_infos)))