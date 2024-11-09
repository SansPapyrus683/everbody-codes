from sys import stdin
from statistics import median

nails = [int(i) for i in stdin.readlines()]
target = int(median(nails))
print(sum(abs(n - target) for n in nails))
