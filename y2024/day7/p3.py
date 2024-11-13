from itertools import combinations

TRACK = """S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-""".split("\n")
ROWS, COLS = len(TRACK), len(TRACK[0])
for r in range(ROWS):
    TRACK[r] = TRACK[r].ljust(COLS)
START = 0, 0

TRACK_SAY = {"+": 1, "-": -1}
OTHERWISE = {"=": 0, **TRACK_SAY}

LOOPS = 2024


def neighbors4(r: int, c: int, r_max: int, c_max: int) -> list[tuple[int, int]]:
    return [p for p in [
        (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
    ] if 0 <= p[0] < r_max and 0 <= p[1] < c_max]



adj = {}
for r in range(ROWS):
    for c in range(COLS):
        if TRACK[r][c] == " ":
            continue
        adj[(r, c)] = [
            (nr, nc) for nr, nc in neighbors4(r, c, ROWS, COLS) if TRACK[nr][nc] != " "
        ]

prev = START
at = 0, 1
path = []
while at != START:
    path.append(at)
    first, second = adj[at]
    old_at = at
    at = first if prev != first else second
    prev = old_at
path.append(START)

opp = input().split(":")[1].replace(",", "")
to_eval = [opp]
for eq_sign in combinations(range(11), 3):
    not_used = list(filter(lambda i: i not in eq_sign, range(11)))
    for minus_sign in combinations(not_used, 3):
        config = []
        for i in range(11):
            if i in eq_sign:
                config.append("=")
            elif i in minus_sign:
                config.append("-")
            else:
                config.append("+")
        to_eval.append("".join(config))

assert LOOPS % 11 == 0

megaloops = LOOPS // 11
mega_len = 11 * len(path)
powers = []
for te in to_eval:
    curr_power = 0
    for i in range(mega_len):
        pos = path[i % len(path)]
        track = TRACK[pos[0]][pos[1]]
        inc = TRACK_SAY[track] if track in TRACK_SAY else OTHERWISE[te[i % len(te)]]
        start = mega_len - i
        curr_power += (megaloops * (mega_len - i) + megaloops * (megaloops - 1) // 2 * mega_len) * inc
    powers.append(curr_power)

print(sum(p > powers[0] for p in powers[1:]))
