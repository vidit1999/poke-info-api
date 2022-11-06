from pydantic import BaseModel, Field

class PokeInfo(BaseModel):
    poke_id: int
    name: str
    abilities: list[str] = []
    types: list[str] = []
