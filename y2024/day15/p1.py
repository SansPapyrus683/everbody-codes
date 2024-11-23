import sys
from collections import deque


def neighbors4(r: int, c: int, r_max: int, c_max: int) -> list[tuple[int, int]]:
    return [p for p in [
        (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
    ] if 0 <= p[0] < r_max and 0 <= p[1] < c_max]


grid = [row.strip() for row in sys.stdin]
row_num = len(grid)
col_num = len(grid[0])

start = None
for c in range(col_num):
    if grid[0][c] == ".":
        start = 0, c
        break

assert start is not None

min_dist = {start: 0}
frontier = deque([start])
while frontier:
    curr = frontier.popleft()
    if grid[curr[0]][curr[1]] == "H":
        print(min_dist[curr] * 2)
        break

    for nr, nc in neighbors4(*curr, row_num, col_num):
        if grid[nr][nc] != "#" and (nr, nc) not in min_dist:
            min_dist[(nr, nc)] = min_dist[curr] + 1
            frontier.append((nr, nc))
