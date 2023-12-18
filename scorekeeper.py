import pygame
from state_manager import *

class Scorekeeper:

    LEFT_PLAYER = 0
    RIGHT_PLAYER = 1

    def __init__(self, state_manager):
        self.scores = [ 0, 0 ]
        self.state_manager = state_manager
        self.score_sound = pygame.mixer.Sound("assets/sounds/mixkit-retro-game-notification-212.wav")

    def award_point(self, which_player):
        self.score_sound.play()
        self.scores[which_player] += 1
        print("Score:", self.scores)
        self.state_manager.set_state(StateManager.GET_READY_STATE)

    def get_score(self, which_player):
        return self.scores[which_player]