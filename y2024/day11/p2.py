import sys

DAYS = 10

babies = {}
for rule in sys.stdin:
    rule = rule.strip()
    split_ind = rule.find(":")
    mom = rule[:split_ind]
    kids = rule[split_ind + 1:].split(",")
    babies[mom] = kids

population = {"Z": 1}
for _ in range(DAYS):
    next_up = {}
    for p, amt in population.items():
        for b in babies[p]:
            if b not in next_up:
                next_up[b] = 0
            next_up[b] += amt
    population = next_up

print(sum(population.values()))
