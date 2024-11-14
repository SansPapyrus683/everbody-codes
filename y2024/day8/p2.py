ACOLYTES = 1111
MARBLE = 20240000

priest_num = int(input())
thickness = 1
layer = 1
used = 1
while used < MARBLE:
    layer += 1
    thickness = (thickness * priest_num) % ACOLYTES
    used += (2 * layer - 1) * thickness

missing = used - MARBLE
print((2 * layer - 1) * missing)
