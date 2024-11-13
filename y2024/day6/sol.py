import sys

ROOT = "RR"
FRUIT = "@"
BAD = {"BUG", "ANT"}

kids = {}
parents = {}
for line in sys.stdin.readlines():
    par, this_kids = line.strip().split(":")
    kids[par] = [k for k in this_kids.split(",") if k not in BAD]

fruit_lens = []
frontier = [ROOT]
come_from = {}
while frontier:
    next_up = []
    fruits = []
    for i in frontier:
        for k in kids.get(i, []):
            if k == FRUIT:
                fruits.append(i)
            else:
                come_from[k] = i
                next_up.append(k)
    if fruits:
        fruit_lens.append(fruits)
    frontier = next_up

take = min(fruit_lens, key=lambda f_: len(f_))[0]
path = [FRUIT]
while take != ROOT:
    path.append(take)
    take = come_from[take]
path.append(ROOT)
path.reverse()

print("using all letters:")
print("".join(path))
print("using only first character:")
print("".join([p[0] for p in path]))
