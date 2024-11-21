import sys


def grid_power(grid: list[str]) -> int:
    pos_at = 1
    power = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != ".":
                continue

            col_chars = {grid[i][c] for i in range(len(grid))}
            row_chars = {grid[r][i] for i in range(len(grid[c]))}
            col_chars.remove(".")
            row_chars.remove(".")
            char = next(iter(col_chars.intersection(row_chars)))
            raw_val = ord(char) - ord("A") + 1
            power += raw_val * pos_at
            pos_at += 1
    return power


groups = []
curr = []
for line in sys.stdin:
    line = line.strip()
    if line:
        curr.append(line)
    else:
        groups.append(curr)
        curr = []
if curr:
    groups.append(curr)

total_power = 0
for g in groups:
    g = [r.split() for r in g]
    grid_num = len(g[0])
    for i in range(grid_num):
        total_power += grid_power([r[i] for r in g])

print(total_power)
