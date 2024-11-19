import sys

DOTS = [1, 3, 5, 10]

brightnesses = [int(b) for b in sys.stdin]
up_to = max(brightnesses)

min_dots = [float("inf") for _ in range(up_to + 1)]
min_dots[0] = 0
for d in DOTS:
    for i in range(d, up_to + 1):
        min_dots[i] = min(min_dots[i], min_dots[i - d] + 1)

print(sum(min_dots[b] for b in brightnesses))
