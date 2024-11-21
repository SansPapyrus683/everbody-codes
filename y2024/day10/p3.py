import sys
from string import ascii_uppercase

SIDE = 8


def grid_power(grid: list[list[str]]) -> int:
    update = True
    chars_left = set(ascii_uppercase)
    for r in range(2, SIDE - 2):
        for c in range(2, SIDE - 2):
            if grid[r][c] != ".":
                chars_left.remove(grid[r][c])

    def set_char(r: int, c: int, to_use: str):
        nonlocal update
        grid[r][c] = to_use
        chars_left.remove(to_use)
        update = True

    while update:
        update = False
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != ".":
                    continue

                col_chars = {grid[i][c] for i in range(len(grid))}
                row_chars = {grid[r][i] for i in range(len(grid[c]))}
                total = (
                    col_chars.intersection(row_chars)
                    .intersection(chars_left)
                    .difference(set(".?"))
                )
                if len(total) == 1:
                    set_char(r, c, next(iter(total)))
                    continue

                row_what = "?" in row_chars
                col_what = "?" in col_chars

                if row_what == col_what == False:
                    return 0
                elif row_what == col_what == True:
                    continue

                if row_what:
                    total = col_chars.intersection(chars_left)
                    if len(total) != 1:
                        continue
                    to_use = next(iter(total))
                    set_char(r, c, to_use)
                    for i in range(len(grid[c])):
                        if grid[r][i] == "?":
                            grid[r][i] = to_use
                            break

                if col_what:
                    total = row_chars.intersection(chars_left)
                    if len(total) != 1:
                        continue
                    to_use = next(iter(total))
                    set_char(r, c, to_use)
                    for i in range(len(grid)):
                        if grid[i][c] == "?":
                            grid[i][c] = to_use
                            break
        
    if any("." in r for r in grid):
        return 0

    power = 0
    pos_at = 1
    for r in range(2, SIDE - 2):
        for c in range(2, SIDE - 2):
            if grid[r][c] != ".":
                power += pos_at * (ord(grid[r][c]) - ord("A") + 1)
                pos_at += 1
    return power


grid = [list(r.strip()) for r in sys.stdin]

total_power = 0
done = set()
for _ in range(10):  # screw this, 10 passes is all you get
    for sr in range(0, len(grid) - 2, SIDE - 2):
        for sc in range(0, len(grid[0]) - 2, SIDE - 2):
            if (sr, sc) in done:
                continue
            
            subgrid = [r[sc : sc + SIDE] for r in grid[sr : sr + SIDE]]
            if (gp := grid_power(subgrid)) != 0:
                total_power += gp
                done.add((sr, sc))
            
            for v, r in enumerate(grid[sr : sr + SIDE]):
                r[sc:sc+SIDE] = subgrid[v]

print(total_power)
