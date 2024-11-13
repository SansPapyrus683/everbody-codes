import sys

SEG_LEN = 10
INIT = 10
DELTA = {"=": 0, "+": 1, "-": -1}

essences = {}
for i in sys.stdin.readlines():
    device, ops = i.strip().split(":")
    ops = ops.split(",")
    period = len(ops)
    while len(ops) < SEG_LEN:
        ops.append(ops[-period])

    power = INIT
    essences[device] = 0
    for o in ops:
        power += DELTA[o]
        essences[device] += power

print("".join(sorted(essences.keys(), key=lambda k: essences[k], reverse=True)))
