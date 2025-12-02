# %%

class DialerAnalyzer:

    def __init__(self, dial_size: int = 100, start_pos: int = 50) -> None:
        self.dial = list(range(dial_size))
        self.current_position = start_pos

    def update_dial_pos(self, new_pos: int):
        projected = self.current_position + new_pos
        if projected >= len(self.dial):
            projected = projected % len(self.dial)
        self.current_position = self.dial[projected]
        return self.current_position

    def analyze_dial_sequence(self, input_seq):
        zeros = []
        for x in input_seq:
            val = int(x.replace("L", "-").replace("R", ""))
            pos = self.update_dial_pos(val)
            if pos == 0:
                zeros.append(x)
        return zeros, len(zeros)


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
da = DialerAnalyzer()
da.analyze_dial_sequence(input_seq)
