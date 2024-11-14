blocks = int(input())

layers = 1
while layers ** 2 < blocks:
    layers += 1

width = 2 * layers - 1
missing = layers ** 2 - blocks
print(width * missing)
