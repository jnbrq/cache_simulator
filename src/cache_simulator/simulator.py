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
        full_assoc_misses = 0
        model_misses = 0
        comp_misses = 0

        # step 1: find the capacity misses
        for event in self._full_assoc_model.simulate(replacement_policy):
            if trace:
                print(event)
            if not event.hit:
                full_assoc_misses += 1
        
        if trace:
            print(f"Fully associative cache misses = { full_assoc_misses }")
            print("===+===+===")
        
        # step 2: find other types of misses
        for event in self._model.simulate(replacement_policy):
            if trace:
                print(event)
            if event.hit:
                hits += 1
            else:
                if event.compulsory:
                    comp_misses += 1
                model_misses += 1
        
        conf_misses = model_misses - full_assoc_misses

        if trace:
            print(f"Model misses = { model_misses }")
            print("===+===+===")
        
        # return the result
        return SimulationResult(hits, comp_misses, conf_misses, model_misses - conf_misses - comp_misses)
