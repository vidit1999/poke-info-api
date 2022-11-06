from dataclasses import dataclass, field, asdict


@dataclass
class PokeInfo:
    poke_id: int
    name: str
    abilities: list[str] = field(default_factory=list)
    types: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)