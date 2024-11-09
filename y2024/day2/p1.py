words = input()[6:].split(",")

input()
helmet = input()
runic = sum(helmet.count(w) for w in words)
print(runic)
