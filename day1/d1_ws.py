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
        # Create a list representing all positions on the dial (0 to size-1)
        self.dial = list(range(size))
        # Track the current position on the dial
        self.current_position = start_position
        # Counter for times the dial lands exactly on position 0
        self.zero_pointings = 0
        # Counter for times the dial crosses over position 0 (currently unused)
        self.zero_crossings = 0

    def count_zero_crossing(
        self, current_pos: int, rotation: int, direction: int
    ) -> int:
        """
        Calculates how many times the dial would cross position 0 during a rotation.

        Args:
            current_pos (int): Current position on the dial
            rotation (int): Total amount of rotation
            direction (int): Direction of rotation (negative for left/counter-clockwise)

        Returns:
            int: Number of times position 0 is crossed
        """
        # If rotating left (negative direction), divide rotation by current position
        # If rotating right (positive direction), divide by distance to complete the circle
        return (
            int(rotation / current_pos)
            if direction < 0
            else int(rotation / (100 - current_pos))
        )

    def update_dial_pos(self, new_pos: int):
        """
        Updates the dial's position and tracks zero crossings.

        Args:
            new_pos (int): The amount to move the dial.
        """
        # Update position using modulo to wrap around the dial
        # Positive values move clockwise, negative values move counter-clockwise
        self.current_position = (self.current_position + new_pos) % len(self.dial)

        # Check if we landed exactly on position 0 and increment counter
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
                # Parse instruction: "L" means negative (left), "R" means positive (right)
                # Replace "L" with "-" to make it negative, remove "R" to keep it positive
                val = int(line.strip().replace("L", "-").replace("R", ""))
                # Apply the movement to the dial
                self.update_dial_pos(val)


def main():
    """
    Main function to run the dial simulation.
    """
    # Create a dial with 100 positions, starting at position 50
    dial_controller = Dial(size=100, start_position=50)

    # Process all instructions from the input file
    dial_controller.process_instructions_from_file("d1.txt")

    # Output the total number of times the dial landed on position 0
    print(dial_controller.zero_pointings)  # Expected answer: 1139


# Example input sequence for testing (commented out)
"""
input_seq = [
    "L68",  # Move left 68 positions
    "L30",  # Move left 30 positions
    "R48",  # Move right 48 positions
    "L5",   # Move left 5 positions
    "R60",  # Move right 60 positions
    "L55",  # Move left 55 positions
    "L1",   # Move left 1 position
    "L99",  # Move left 99 positions
    "R14",  # Move right 14 positions
    "L82",  # Move left 82 positions
]
"""

# Entry point: run main() when script is executed directly
if __name__ == "__main__":
    main()
