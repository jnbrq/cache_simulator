from dataclasses import dataclass
from typing import List
from .model import Model
from .replacement_policy import ReplacementPolicy

@dataclass(frozen=True)
class SimulationResult:
    hits: int
    compulsory_misses: int
    conflict_misses: int
    capacity_misses: int

    def total_accesses(self) -> int:
        return self.hits + self.total_misses()
    
    def total_misses(self) -> int:
        return self.compulsory_misses + self.conflict_misses + self.capacity_misses

    def hit_ratio(self) -> float:
        return self.hits / self.total_accesses()
    
    def miss_ratio(self) -> float:
        return 1 - self.hit_ratio()


class Simulator:
    def __init__(self, model: Model) -> None:
        self._model = model
        self._full_assoc_model = Model(0, model.no_ways() * model.no_sets())
    
    def simulate(self, access_seq: List[int], replacement_policy: ReplacementPolicy, trace=False) -> SimulationResult:
        self._model.reset()
        self._full_assoc_model.reset()

        for access in access_seq:
            self._model.access(access)
            self._full_assoc_model.access(access)

        hits = 0
        compulsory_misses = 0
        conflict_misses = 0
        capacity_misses = 0

        # step 1: find the capacity misses
        for event in self._full_assoc_model.simulate(replacement_policy):
            if not event.hit and not event.compulsory:
                capacity_misses += 1
        
        # step 2: find other types of misses
        for event in self._model.simulate(replacement_policy):
            if trace:
                print(event)
            if event.hit:
                hits += 1
            elif event.compulsory:
                compulsory_misses += 1
            else:
                conflict_misses += 1
        conflict_misses -= capacity_misses

        # return the result
        return SimulationResult(hits, compulsory_misses, conflict_misses, capacity_misses)
