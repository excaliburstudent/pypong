class ScoreKeeper:

    LEFT_PLAYER = 0
    RIGHT_PLAYER = 1

    def __init__(self):
        self.scores = [ 0, 0 ]

    def award_point(self, which_player):
        self.scores[which_player] += 1
        print("Score:", self.scores)