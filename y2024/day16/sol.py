import sys
from collections import Counter

FACE_LEN = 3
P1_PULLS = 100
P2_PULLS = 202420242024
P3_PULLS = 256


def coin_value(pos: list[int], segments: list[list[str]]) -> int:
    char_freq = Counter(
        "".join(segments[t][p][0] + segments[t][p][2] for t, p in enumerate(pos))
    )
    return sum(max(0, f - 2) for f in char_freq.values())


turns = [int(i) for i in input().split(",")]
input()

segments = [[] for _ in range(len(turns))]
for line in sys.stdin:
    line = line.rstrip()
    at = 0
    for t in range(len(turns)):
        if at >= len(line):
            break
        segments[t].append(line[at : at + FACE_LEN])
        at += FACE_LEN + 1

for t in range(len(turns)):
    segments[t] = [s for s in segments[t] if not s.isspace()]

p1_res = []
# could make this a list comp, but idrc
for t in range(len(turns)):
    p1_res.append(segments[t][(turns[t] * P1_PULLS) % len(segments[t])])
print(f"after {P1_PULLS} pulls: {' '.join(p1_res)}")

start = [0 for _ in range(len(turns))]
coins = []
at = start.copy()
init = True
while at != start or init:
    init = False
    at = [(p + turns[t]) % len(segments[t]) for t, p in enumerate(at)]
    coins.append(coin_value(at, segments))

cycles, pulls_left = divmod(P2_PULLS, len(coins))
total_earnings = sum(coins) * cycles + sum(coins[:pulls_left])
print(f"earnings after {P2_PULLS} pulls: {total_earnings}")

frontier = {tuple(start): (0, 0)}
for _ in range(P3_PULLS):
    next_up = {}
    for at, bounds in frontier.items():
        down, up, nope = [], [], []
        for t, p in enumerate(at):
            down.append((p + 1 + turns[t]) % len(segments[t]))
            up.append((p - 1 + turns[t]) % len(segments[t]))
            nope.append((p + turns[t]) % len(segments[t]))
    
        for i in [down, up, nope]:
            i = tuple(i)
            get_coins = coin_value(i, segments)

            lb, ub = bounds[0] + get_coins, bounds[1] + get_coins
            if i not in next_up:
                next_up[i] = lb, ub
            else:
                prev_lb, prev_ub = next_up[i]
                next_up[i] = min(prev_lb, lb), max(prev_ub, ub)

    frontier = next_up

worst = min(e[0] for e in frontier.values())
best = max(e[1] for e in frontier.values())
print(f"max & min after {P3_PULLS} pulls: {best} {worst}")
