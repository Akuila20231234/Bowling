class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for _ in range(10):
            if self.is_strike(roll_index):
                total_score += self.strike_score(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += self.spare_score(roll_index)
                roll_index += 2

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def stickeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
