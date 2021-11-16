import os
import sys

def set_path():
    folder, file = os.path.split(__file__)
    sys.path = [ folder + "/../src" ] + sys.path

set_path()

from cache_simulator import *

print(Simulator(
    # Cache model (log number of sets, associativity)
    Model(1, 1))
    .simulate(
        # access sequence
        [2,3,4,3,0,1,0,3,0,3,1,2,3,0,2,3],
        # replacement policy
        LRUReplacementPolicy(),
        # the whole trace
        trace=True))
