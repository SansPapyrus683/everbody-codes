import sys

words = input()[6:].split(",")
for w in words.copy():
    words.append(w[::-1])
words.sort(key=lambda rune: len(rune), reverse=True)

input()
runic = 0
for line in sys.stdin:
    line = line.strip()
    is_symbol = [False for _ in range(len(line))]
    for i in range(len(line)):
        for w in words:
            if line[i:].startswith(w):
                for j in range(i, i + len(w)):
                    is_symbol[j] = True
                break
    runic += sum(is_symbol)

print(runic)
