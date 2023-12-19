import pygame
import time

class StateManager:

    GET_READY_STATE = 0
    PLAYING_STATE = 1
    GAME_OVER_STATE = 2

    GET_READY_STATE_MESSAGE = "Get Ready!"
    GET_READY_STATE_DURATION = 3  # seconds

    GAME_OVER_STATE_MESSAGE = "GAME OVER --- Press SPACE to play again"

    def __init__(self, message_board):
        self.message_board = message_board
        self.set_state(StateManager.GET_READY_STATE)

    def set_state(self, state):
        if not hasattr(self, "state") or state != self.state:
            self.state = state

            if self.state == StateManager.GET_READY_STATE:
                self.message_board.set_message(StateManager.GET_READY_STATE_MESSAGE)
                self.start_time = time.time()
            elif self.state == StateManager.GAME_OVER_STATE:
                pygame.mixer.Sound("assets/sounds/mixkit-arcade-retro-game-over-213.wav").play()
                self.message_board.set_message(StateManager.GAME_OVER_STATE_MESSAGE)
            else:
                self.message_board.clear_message()

    def get_state(self):
        return self.state
    
    def update(self):
        if self.state == StateManager.GET_READY_STATE:
            if time.time() - self.start_time > StateManager.GET_READY_STATE_DURATION:
                self.set_state(StateManager.PLAYING_STATE)