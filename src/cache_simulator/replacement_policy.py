from abc import ABC, abstractmethod
from typing import List
from .block import Block

class ReplacementPolicy(ABC):
    @abstractmethod
    def replace_index(self, l: List[Block]) -> int:
        pass
    
    @abstractmethod
    def access(self, block: Block):
        pass

    @abstractmethod
    def reset(self):
        pass
