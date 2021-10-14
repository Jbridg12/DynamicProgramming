import sys
import numpy as np

gamma = 0.9
threshold = 0.0001
class State:
    def __init__(self, taken, mask, index):
        self.taken = taken
        self.mask = mask
        self.index = index
        self.value = 0.0
        self.policy = "move"
        
        
N = int(sys.argv[1])
ptaken = float(sys.argv[2])
pmask = float(sys.argv[3])
psick_empty = float(sys.argv[4])
psick_masked = float(sys.argv[5])
psick_nomask = float(sys.argv[6])
rsick = float(sys.argv[7])
rexit = float(sys.argv[8])
rlearn = float(sys.argv[9])


states = []
for i in range(1, N+1):
    states.insert(0, [State(False, True, i), State(True, True, i), State(True, False, i)])


def CalcValue(state, action):
    if action == "move":
        if state.index == 1:
            return rexit
        else:
            nt = (1-ptaken)*(gamma*states[state.index-1][0].value)
            tm = ((ptaken*pmask)/ptaken)*(gamma*states[state.index-1][1].value)
            tnm = ((ptaken*(1-pmask))/ptaken)*(gamma*states[state.index-1][2].value)
            return nt+tm+tnm        
    elif action == "sit":
        if state.taken:
            if state.mask:
                return (psick_masked * rsick) + ((1-psick_masked) * (rlearn*(N-state.index)))
            else:
                return (psick_nomask * rsick) + ((1-psick_nomask) * (rlearn*(N-state.index)))
        else:
            return (psick_empty * rsick) + ((1-psick_empty) * (rlearn*(N-state.index)))
    return 
    

   
def ValueIteration():
    while True:
        delta = 0
        for ele in states:
            for s in ele:
                v = s.value
                s.value = min(CalcValue(s, "move"), CalcValue(s, "stay")) 
                error = abs(v-s.value)
                if(error > delta):
                    delta = error
        
        if delta >= threshold:
            break

def PolicyImprov(valuefunc):
    return 1