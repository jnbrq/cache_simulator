import os
import sys

def set_path():
    folder, file = os.path.split(__file__)
    sys.path = [ folder + "/../src" ] + sys.path

set_path()

from cache_simulator import *

print(Simulator(
    # Cache model (log number of sets, associativity)
    Model(1, 2))
    .simulate(
        # access sequence
        [2,2,5,3,0,5,0,3,5,0,0,4,1,2,5,1],
        # replacement policy
        LRUReplacementPolicy(),
        # the whole trace
        trace=True))

