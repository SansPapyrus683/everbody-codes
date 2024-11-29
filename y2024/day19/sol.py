import sys
from math import ceil, log2
from copy import deepcopy

P1_AMT = 1
P2_AMT = 100
P3_AMT = 1048576000

# the order of this list actually matters lmao
AROUND = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

dirs = input()
input()

grid = [list(line.strip()) for line in sys.stdin]
just_pos = [[(r, c) for c in range(len(grid[r]))] for r in range(len(grid))]

at = 0
for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[r]) - 1):
        cells = [just_pos[r + x][c + y] for x, y in AROUND]
        delta = -1 if dirs[at] == "L" else 1
        for v, (dr, dc) in enumerate(AROUND):
            new_pos = AROUND[(v + delta) % len(AROUND)]
            just_pos[r + new_pos[0]][c + new_pos[1]] = cells[v]
        at = (at + 1) % len(dirs)

go_to = {}
binary_ends = {}
max_dist = max(ceil(log2(d)) for d in [P1_AMT, P2_AMT, P3_AMT])
for r in range(len(grid)):
    for c in range(len(grid[r])):
        go_to[just_pos[r][c]] = r, c
        binary_ends[just_pos[r][c]] = [(r, c)] + [None for _ in range(max_dist)]

for i in range(1, max_dist + 1):
    for pos, ends in binary_ends.items():
        ends[i] = binary_ends[ends[i - 1]][i - 1]

for d in [P1_AMT, P2_AMT, P3_AMT]:
    new_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            at = r, c
            for pow_ in range(max_dist, -1, -1):
                if (d & (1 << pow_)) != 0:
                    at = binary_ends[at][pow_]
            new_grid[at[0]][at[1]] = grid[r][c]
    
    print(f"grid after {d} steps:")
    for row in new_grid:
        print("".join(row))
