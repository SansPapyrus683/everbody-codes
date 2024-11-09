import sys

words = input()[6:].split(",")
for w in words.copy():
    words.append(w[::-1])
words.sort(key=lambda rune: len(rune), reverse=True)

input()
grid = [line.strip() for line in sys.stdin.readlines()]

row_num = len(grid)
col_num = len(grid[0])  # just shrothands
is_symbol = [[False for _ in range(col_num)] for i in range(row_num)]

for r in range(row_num):
    for c in range(col_num):
        right = grid[r][c:] + grid[r][:c]
        for w in words:
            if right.startswith(w):
                for c_ in range(c, c + len(w)):
                    is_symbol[r][c_ % col_num] = True
                break

        down = "".join(grid[r_][c] for r_ in range(r, row_num))
        for w in words:
            if down.startswith(w):
                for r_ in range(r, r + len(w)):
                    is_symbol[r_][c] = True
                break

total_runes = sum(sum(r) for r in is_symbol)
print(total_runes)
