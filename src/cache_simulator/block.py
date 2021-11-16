from dataclasses import InitVar, dataclass

@dataclass(unsafe_hash=True)
class Block:
    tag: int
    set: int
    model: InitVar["Model"]

    def __post_init__(self, model: "Model") -> None:
        self.address = (self.tag << (model.log_sets()) | self.set)

    def __repr__(self) -> str:
        return f"Block({self.tag}, {self.set}, #{self.address})"
    
    @staticmethod
    def from_address(model: "Model", address: int) -> "Block":
        tag = address >> (model.log_sets())
        set = (address) & ((1 << model.log_sets()) - 1)
        return Block(tag, set, model)
