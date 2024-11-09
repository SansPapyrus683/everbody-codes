import sys
from copy import deepcopy


def neighbors8(r: int, c: int, r_max: int, c_max: int) -> list[tuple[int, int]]:
    return [p for p in [
        (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
        (r + 1, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1),
    ] if 0 <= p[0] < r_max and 0 <= p[1] < c_max]


# i mean adding a boundary of falses is the quickest thing i could think of
grid = [[False] + [i == "#" for i in line.strip()] + [False] for line in sys.stdin.readlines()]
col_num = len(grid[0])
grid = [[False] * col_num] + grid + [[False] * col_num]
row_num = len(grid)

blocks_left = sum(sum(r) for r in grid)
max_removed = 0
while blocks_left:
    max_removed += blocks_left

    new_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if any(not grid[nr][nc] for nr, nc in neighbors8(r, c, row_num, col_num)):
                new_grid[r][c] = False

    grid = new_grid
    blocks_left = sum(sum(r) for r in grid)

print(max_removed)
