from typing import Dict, List
from ..block import Block
from ..replacement_policy import ReplacementPolicy

class OptimalReplacementPolicy(ReplacementPolicy):
    # TODO IMPLEMENT ME

    def __init__(self) -> None:
        super().__init__()
        self.reset()

    def replace_index(self, l: List[Block]) -> int:
        pass
    
    def access(self, block: Block):
        pass
    
    def reset(self):
        pass

