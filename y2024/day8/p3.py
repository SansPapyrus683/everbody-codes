ACOLYTES = 10
PLATINUM = 202400000


def blocks_needed(layers: int, priests: int):
    thickness = [1]
    layer = 1
    used = 1
    for _ in range(layers - 1):
        layer += 1
        thickness.append((thickness[-1] * priests) % ACOLYTES + ACOLYTES)
        used += (2 * layer - 1) * thickness[-1]

    width = 2 * layer - 1
    heights = [0 for _ in range(width)]
    for v, t in enumerate(thickness):
        for i in range(layer - 1 - v, layer + v):
            heights[i] += t

    needed = sum(heights)
    for h in heights[1:-1]:
        needed -= priests * width * h % ACOLYTES
    return needed


priest_num = int(input())

lo = 1
hi = 10 ** 4
valid = -1
while lo <= hi:
    mid = (lo + hi) // 2
    res = blocks_needed(mid, priest_num)
    if res < PLATINUM:
        valid = mid
        lo = mid + 1
    else:
        hi = mid - 1

bit_more = blocks_needed(valid + 1, priest_num)
print(bit_more - PLATINUM)
