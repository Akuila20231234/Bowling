class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0
        """
        __init__ method:
        Parameter: self
        This initializes an instance of the BowlingGame class and creates an empty list called rolls to store the pins knocked down in each roll.

        roll method:
        Parameters: self, pins
        Argument (example): pins (e.g., when calling game.roll(5))
        This method records the result of a roll by appending the number of pins knocked down (passed as the argument pins) to the rolls list.

        score method:
        Parameter: self
        The score method is intended to calculate the total score of the game. The variables total_score and roll_index are initialized to keep track of the total score and the current roll being processed, respectively. The for loop is likely intended to loop through the 10 frames of a bowling game, though the loop itself is incomplete in the provided code.
        """
        
        for _ in range(10):
            if self.is_strike(roll_index):
                total_score += self.strike_score(roll_index)
                roll_index += 1
                """

                """
            elif self.is_spare(roll_index):
                total_score += self.spare_score(roll_index)
                roll_index += 2
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2

        return total_score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_score(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_score(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]