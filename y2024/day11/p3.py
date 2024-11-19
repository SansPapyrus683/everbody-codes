import sys

DAYS = 20

babies = {}
for rule in sys.stdin:
    rule = rule.strip()
    split_ind = rule.find(":")
    mom = rule[:split_ind]
    kids = rule[split_ind + 1:].split(",")
    babies[mom] = kids

ending_pops = []
for starting in babies:
    population = {starting: 1}
    for _ in range(DAYS):
        next_up = {}
        for p, amt in population.items():
            for b in babies[p]:
                if b not in next_up:
                    next_up[b] = 0
                next_up[b] += amt
        population = next_up
    ending_pops.append(sum(population.values()))

print(max(ending_pops) - min(ending_pops))
