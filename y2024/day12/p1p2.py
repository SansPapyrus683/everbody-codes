"""p2 is just a more general version of p1 so..."""

import sys

SEG = {"A": 1, "B": 2, "C": 3}

grid = list(sys.stdin)
starts = []
marks = []
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] in SEG:
            starts.append(((r, c), SEG[grid[r][c]]))
        elif grid[r][c] == "T":
            marks.append((r, c))
        elif grid[r][c] == "H":
            marks.append((r, c))
            marks.append((r, c))

max_pow = len(grid)
tot = 0
for m in marks:
    for s, val in starts:
        for p in range(1, max_pow + 1):
            end_ = s[0] - p, s[1] + 2 * p
            dr = m[0] - end_[0]
            dc = m[1] - end_[1]
            if dr == dc and dr >= 0:
                tot += p * val
                break
        else:
            continue

        break

print(tot)
