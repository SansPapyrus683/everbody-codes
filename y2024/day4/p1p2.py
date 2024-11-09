"""man the bounds this problem gives are like so small what the hell"""
from sys import stdin

nails = [int(i) for i in stdin.readlines()]
lowest = min(nails)
print(sum(n - lowest for n in nails))
