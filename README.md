# cache_simulator

This is a simple cache simulator written in Python3 that can output the following metrics given the access sequence and cache structure:

- Hit rate
- Number of compulsory misses
- Number of capacity misses
- Number of conflict misses

## Installation

    python3 -m pip install --upgrade --force-reinstall git+https://github.com/jnbrq/cache_simulator

## Usage

You can easily import the package and simulate with:

    from cache_simulator import *

    print(Simulator(
        # Cache model (log number of sets, associativity)
        Model(1, 2))
        .simulate(
            # access sequence
            [7, 19, 14, 2, 14, 14, 2, 19, 10, 19, 1, 2],
            # replacement policy
            LRUReplacementPolicy(),
            # the whole trace
            trace=True))

## Available Replacement Policies

- `FIFOReplacementPolicy`
- `LRUReplacementPolicy`
- `MRUReplacementPolicy`
- `OptimalReplacementPolicy` (to be implemented)
