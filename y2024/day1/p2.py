COSTS = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

monsters = input()
cost = 0
for i in range(0, len(monsters), 2):
    a, b = monsters[i], monsters[i + 1]
    cost += COSTS[a] + COSTS[b]
    if "x" not in [a, b]:
        cost += 2

print(cost)
