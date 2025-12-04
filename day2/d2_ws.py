# %%

current_pos = 82
max = 100
direction = 1


def count_zero_crossing(current_pos: int, rotation: int, direction: int) -> int:
    return (
        int(rotation / current_pos)
        if direction < 0
        else int(rotation / (100 - current_pos))
    )


# %%
"""
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
"""
direction = 1
rotation = 280
count_zero_crossing(current_pos, rotation, direction)
