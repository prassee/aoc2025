class Dial:
    """
    A class to represent a circular dial that can be rotated.
    """

    def __init__(self, size=100, start_position=50):
        """
        Initializes the Dial.

        Args:
            size (int): The number of positions on the dial.
            start_position (int): The initial position on the dial.
        """
        self.dial = list(range(size))
        self.current_position = start_position
        self.zero_pointings = 0
        self.zero_crossings = 0

    def update_dial_pos(self, new_pos: int):
        """
        Updates the dial's position and tracks zero crossings.

        Args:
            new_pos (int): The amount to move the dial.
        """
        self.current_position = (self.current_position + new_pos) % len(self.dial)
        if self.current_position == 0:
            self.zero_pointings += 1
        return self.current_position

    def process_instructions_from_file(self, filename: str):
        """
        Processes a sequence of movements from a file.

        Args:
            filename (str): The name of the file with instructions.
        """
        with open(filename) as f:
            for line in f:
                val = int(line.strip().replace("L", "-").replace("R", ""))
                self.update_dial_pos(val)


def main():
    """
    Main function to run the dial simulation.
    """
    dial_controller = Dial(size=100, start_position=50)
    dial_controller.process_instructions_from_file("d1.txt")
    print(dial_controller.zero_pointings)  # 1139


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
if __name__ == "__main__":
    main()
