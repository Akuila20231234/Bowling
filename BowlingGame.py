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
                Arguments: 
                is_strike
                strike_score

                Parameter: 
                if self.is_strike(roll_index):
                This condition checks if the current roll, referenced by roll_index, is a strike (when all 10 pins are knocked down on the first roll of the frame). If it is, the code proceeds with the strike logic.
                
                total_score += self.strike_score(roll_index):
                If a strike is detected, the strike_score method is called to calculate the score for the strike (usually 10 plus the sum of the next two rolls), and this score is added to total_score.
                
                roll_index += 1
                After processing a strike, roll_index is incremented by 1 to move to the next roll. In the case of a strike, only one roll is counted for the frame.
                """
            elif self.is_spare(roll_index):
                total_score += self.spare_score(roll_index)
                roll_index += 2

                """
                elif self.is_spare(roll_index):
                This condition checks if the current frame, starting at roll_index, is a spare. A spare occurs when all 10 pins are knocked down in two rolls within the frame.
               
                total_score += self.spare_score(roll_index):
                If a spare is detected, the spare_score method is called to calculate the score for the spare. In bowling, the score for a spare is 10 plus the number of pins knocked down in the next roll. The result is added to total_score.
                
                roll_index += 2:
                After processing a spare, roll_index is incremented by 2 to move to the next frame, as a spare consumes two rolls within the current frame.
                """
            else:
                total_score += self.frame_score(roll_index)
                roll_index += 2
                """
                else:
                This handles the case where the current frame is neither a strike nor a spare. It processes a normal frame where the player needed two rolls to knock down all the pins (or failed to knock them all down).
                
                total_score += self.frame_score(roll_index):
                The frame_score method is called to calculate the total pins knocked down in the current frame (two rolls). The sum of the pins from both rolls in the frame is added to total_score.
                
                roll_index += 2:
                Since a regular frame consists of two rolls, roll_index is incremented by 2 to move to the next frame.
                """

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
    
    """
    is_strike(self, roll_index)
    Checks if the roll at roll_index is a strike (i.e., if it knocked down all 10 pins). Returns True if it is a strike, otherwise False.
    
    is_spare(self, roll_index)
    Checks if the sum of the pins knocked down in the roll at roll_index and the next roll (at roll_index + 1) equals 10. Returns True if it’s a spare, otherwise False.
    
    strike_score(self, roll_index)
    Calculates the score for a strike. A strike is worth 10 points plus the total pins knocked down in the next two rolls (at roll_index + 1 and roll_index + 2).
    
    spare_score(self, roll_index)
    Calculates the score for a spare. A spare is worth 10 points plus the total pins knocked down in the roll immediately following the spare (at roll_index + 2).
    
    frame_score(self, roll_index)
    Calculates the score for a regular frame. This method sums up the pins knocked down in the roll at roll_index and the next roll (at roll_index + 1).
    """