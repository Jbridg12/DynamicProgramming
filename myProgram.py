import sys
import numpy as np


N = sys.argv[1]
ptaken = sys.argv[2]
pmask = sys.argv[3]
psick_empty = sys.argv[4]
psick_masked = sys.argv[5]
psick_nomask = sys.argv[6]
rsick = sys.argv[7]
rexit = sys.argv[8]
rlearn = sys.argv[9]

states = [3][N]

def State():
    def __init__(self, taken, mask, index):
        self.taken = taken
        self.mask = mask
        self.index = index
        self.value = 0

def CalcValue(state, action):
    if action == "move":
        if state.index == N-1:
            nt = (1-ptaken)
        else:    
            nt = (1-ptaken)(0+
    if state.taken:
        if state.mask:
            
        else:
    else:
    res = valuefunc[]
    return 1
    
def ValueIteration():
    return 1

def PolicyImprov(valuefunc):
    return 1