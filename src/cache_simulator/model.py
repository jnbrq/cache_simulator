from replacement_policy import ReplacementPolicy
from typing import Iterator, Union, Tuple
from events import HitEvent, MissEvent
from block import Block

class Model:
    def __init__(self, log_sets: int, no_ways: int) -> None:
        """
        Constructs a cache structure.
        """
        self._log_sets = log_sets
        self._no_ways = no_ways
        self.reset()
    
    def log_sets(self) -> int:
        return self._log_sets
    
    def no_sets(self) -> int:
        return 1 << self._log_sets
    
    def no_ways(self) -> int:
        return self._no_ways
    
    def reset(self) -> None:
        self._accesses = []
    
    def access(self, address: int) -> None:
        """
        Records an access. Accesses are sequential.
        """
        self._accesses.append(address)
    
    def simulate(self, replacement_policy: ReplacementPolicy) -> Iterator[Union[HitEvent, MissEvent]]:
        """
        Simulates and yields a `HitEvent` or `MissEvent`.
        """

        # reset the policy
        replacement_policy.reset()

        # create a cache state
        state = [ [ None ] * self.no_ways() for i in range(self.no_sets()) ]

        # create a list of blocks that we encountered
        encountered_blocks = set()

        def check_block(block: Block) -> Tuple[bool, int]:
            for b in state[block.set]:
                if b is not None:
                    if b == block:
                        return True
            return False

        for address in self._accesses:
            block = Block.from_address(self, address)
            compulsory = False
            if not block in encountered_blocks:
                compulsory = True
                encountered_blocks.add(block)
            if check_block(block):
                yield HitEvent(block)
            else:
                placed = False
                for i, b in enumerate(state[block.set]):
                    if b is None:
                        state[block.set][i] = block
                        yield MissEvent(block, i, None, compulsory)
                        placed = True
                        break
                if not placed:
                    # replace a block
                    idx = replacement_policy.replace_index(state[block.set])
                    yield MissEvent(block, idx, state[block.set][idx], compulsory)
                    state[block.set][idx] = block
            replacement_policy.access(block)

