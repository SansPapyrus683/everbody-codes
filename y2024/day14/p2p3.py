import sys
from collections import deque

DIRS = {
    "U": (0, 1, 0),
    "R": (1, 0, 0),
    "L": (-1, 0, 0),
    "D": (0, -1, 0),
    "F": (0, 0, 1),
    "B": (0, 0, -1),
}


def neighbors4(x: int, y: int, z: int) -> list[tuple[int, int, int]]:
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


plant = set()
leaves = []
for branch in sys.stdin:
    branch = branch.strip().split(",")
    at = (0, 0, 0)
    for v, i in enumerate(branch):
        d = DIRS[i[0]]
        amt = int(i[1:])
        for _ in range(amt - (v == 0)):
            at = at[0] + d[0], at[1] + d[1], at[2] + d[2]
            plant.add(at)
    leaves.append(at)

print(f"total # of segments in plant: {len(plant)}")

best = float("inf")
for i in plant:
    if i[0] != 0 or i[2] != 0:
        continue

    frontier = deque([i])
    min_dist = {i: 0}
    while frontier:
        curr = frontier.popleft()
        for n in neighbors4(*curr):
            if n in plant and n not in min_dist:
                min_dist[n] = min_dist[curr] + 1
                frontier.append(n)

    murky = sum(min_dist[l] for l in leaves)
    best = min(best, murky)

print(f"min murkiness: {best}")
