import sys
import heapq
from collections import defaultdict


def neighbors4(r: int, c: int) -> list[tuple[int, int]]:
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def transfer_cost(h1: int, h2: int) -> int:
    if h1 > h2:
        return transfer_cost(h2, h1)
    return min(h2 - h1, 10 - h2 + h1)


grid = {}
starts = []
end = None
for r, row in enumerate(sys.stdin):
    for c, char in enumerate(row):
        if char == "S":
            starts.append((r, c))
            grid[(r, c)] = 0
        elif char == "E":
            end = r, c
            grid[(r, c)] = 0
        elif char.isdigit():
            grid[(r, c)] = int(char)

frontier = []
min_dist = defaultdict(lambda: float("inf"))
for s in starts:
    min_dist[s] = 0
    frontier.append((0, s))

while frontier:
    c_dist, curr = heapq.heappop(frontier)
    if c_dist > min_dist[curr]:
        continue

    if curr == end:
        break

    for n in neighbors4(*curr):
        if n not in grid:
            continue

        n_dist = c_dist + transfer_cost(grid[curr], grid[n]) + 1
        if n_dist < min_dist[n]:
            min_dist[n] = n_dist
            heapq.heappush(frontier, (n_dist, n))

print(min_dist[end])
