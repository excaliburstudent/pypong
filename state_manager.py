import time

class StateManager:

    GET_READY_STATE = 0
    PLAYING_STATE = 1

    GET_READY_STATE_MESSAGE = "Get Ready!"
    GET_READY_STATE_DURATION = 3  # seconds

    def __init__(self, message_board):
        self.message_board = message_board
        self.set_state(StateManager.GET_READY_STATE)

    def set_state(self, state):
        self.state = state

        if self.state == StateManager.GET_READY_STATE:
            self.message_board.set_message(StateManager.GET_READY_STATE_MESSAGE)
            self.start_time = time.time()
        else:
            self.message_board.clear_message()

    def get_state(self):
        return self.state
    
    def update(self):
        if self.state == StateManager.GET_READY_STATE:
            if time.time() - self.start_time > StateManager.GET_READY_STATE_DURATION:
                self.set_state(StateManager.PLAYING_STATE)