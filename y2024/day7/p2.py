import sys

LOOPS = 10
INIT = 10
TRACK = """S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-""".split("\n")
ROWS, COLS = len(TRACK), len(TRACK[0])

TRACK_SAY = {"+": 1, "-": -1}
OTHERWISE = {"=": 0, **TRACK_SAY}

loop_len = ROWS * 2 + (COLS - 2) * 2

essences = {}
for i in sys.stdin.readlines():
    device, ops = i.strip().split(":")
    ops = ops.split(",")
    ops_at = 0
    track_at = [0, 1]

    essences[device] = 0
    power = INIT
    for _ in range(loop_len * LOOPS):
        track = TRACK[track_at[0]][track_at[1]]
        power += TRACK_SAY[track] if track in TRACK_SAY else OTHERWISE[ops[ops_at]]

        ops_at = (ops_at + 1) % len(ops)
        if track_at[0] == 0 and track_at[1] + 1 < COLS:
            track_at[1] += 1
        elif track_at[1] == COLS - 1 and track_at[0] + 1 < ROWS:
            track_at[0] += 1
        elif track_at[0] == ROWS - 1 and track_at[1] - 1 >= 0:
            track_at[1] -= 1
        elif track_at[1] == 0 and track_at[0] - 1 >= 0:
            track_at[0] -= 1

        essences[device] += power

print("".join(sorted(essences.keys(), key=lambda k: essences[k], reverse=True)))
