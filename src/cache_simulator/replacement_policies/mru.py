from typing import Dict, List
from ..block import Block
from ..replacement_policy import ReplacementPolicy

class MRUReplacementPolicy(ReplacementPolicy):
    def __init__(self) -> None:
        super().__init__()
        self.reset()

    def replace_index(self, l: List[Block]) -> int:
        # find the one that was least recently accessed
        lru_idx = 0
        lru_t = self._access_t[l[lru_idx]]

        for idx, b in enumerate(l):
            t = self._access_t[b]
            if t > lru_t:
                lru_idx = idx
                lru_t = t
        
        return lru_idx
    
    def access(self, block: Block):
        self._access_t[block] = self._t
        self._t += 1
    
    def reset(self):
        self._t: int = 0
        self._access_t: Dict[Block, int] = {  }
