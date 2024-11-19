import sys
from collections import defaultdict

LOOP_THRESH = 1000

mat = [[int(i) for i in r.split()] for r in sys.stdin]
cols = [[mat[r][c] for r in range(len(mat))] for c in range(len(mat[0]))]

i = 0
seen = defaultdict(int)
while LOOP_THRESH not in seen.values():
    clapper = cols[i % len(cols)].pop(0)
    next_col = cols[(i + 1) % len(cols)]

    end_pos = (clapper - 1) % (2 * len(next_col))
    if end_pos < len(next_col):
        next_col.insert(end_pos, clapper)
    else:
        new_ind = len(next_col) - (end_pos - len(next_col))
        next_col.insert(new_ind, clapper)

    seen[int("".join(str(c[0]) for c in cols))] += 1
    i += 1

print(max(seen))
