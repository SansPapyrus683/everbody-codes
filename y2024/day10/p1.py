import sys

grid = [row.strip() for row in sys.stdin]

runic_word = []
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] != ".":
            continue
        col_chars = {grid[i][c] for i in range(len(grid))}
        row_chars = {grid[r][i] for i in range(len(grid[c]))}
        col_chars.remove(".")
        row_chars.remove(".")
        runic_word.append(next(iter(col_chars.intersection(row_chars))))

print("".join(runic_word))
