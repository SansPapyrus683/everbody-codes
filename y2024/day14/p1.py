height = 0
tallest = 0
for part in input().split(","):
    d = part[0]
    amt = int(part[1:])
    if d == "U":
        height += amt
    elif d == "D":
        height -= amt
    tallest = max(tallest, height)

print(tallest)
