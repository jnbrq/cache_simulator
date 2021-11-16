from dataclasses import dataclass, field
from .block import Block

@dataclass(frozen=True)
class HitEvent:
    block: Block
    hit: bool = field(default=True, init=False)

@dataclass(frozen=True)
class MissEvent:
    block: Block
    way: int
    replaced_block: Block
    compulsory: bool
    hit: bool = field(default=False, init=False)
