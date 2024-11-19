import sys

DAYS = 4

babies = {}
for rule in sys.stdin:
    rule = rule.strip()
    split_ind = rule.find(":")
    mom = rule[:split_ind]
    kids = rule[split_ind + 1:].split(",")
    babies[mom] = kids

# eh, brute force works for now
population = ["A"]
for _ in range(DAYS):
    next_up = []
    for p in population:
        next_up.extend(babies[p])
    population = next_up

print(len(population))
