COSTS = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

monsters = input()
cost = 0
for i in range(0, len(monsters), 3):
    triplet = monsters[i:i+3]
    amt = len(triplet) - triplet.count("x")
    cost += sum(COSTS[c] for c in triplet) + amt * max(0, amt - 1)

print(cost)
