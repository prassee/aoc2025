# %%
dial = list(range(0, 100))
current_position = 50


def update_dial_pos(new_pos: int):
    global current_position
    projected = current_position + new_pos
    if projected >= len(dial):
        projected = projected % len(dial)
    current_position = dial[projected]
    print(f"current position {current_position}")


# %%
input_seq = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]
for x in input_seq:
    val = int(x.replace("L", "-").replace("R", ""))
    update_dial_pos(val)
