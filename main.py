import pygame
import colors
from court import *
from paddle import *
from ball import *
from scorekeeper import *
from scoreboard import *
from message_board import *
from state_manager import *

WIDTH = 800
HEIGHT = 600
SCOREBOARD_HEIGHT = 100
BOTTOM_PANEL_HEIGHT = 50
FRAME_RATE = 30
WINNING_SCORE = 9

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

message_board = MessageBoard(0, HEIGHT - BOTTOM_PANEL_HEIGHT, WIDTH, BOTTOM_PANEL_HEIGHT)
state_manager = StateManager(message_board)
scorekeeper = Scorekeeper(state_manager)
scoreboard = Scoreboard(scorekeeper, 0, 0, WIDTH, SCOREBOARD_HEIGHT, colors.BLUE, colors.RED)
court = Court(0, SCOREBOARD_HEIGHT, WIDTH, HEIGHT - SCOREBOARD_HEIGHT - BOTTOM_PANEL_HEIGHT)
left_paddle = Paddle(court, Court.LEFT_PADDLE, colors.BLUE)
right_paddle = Paddle(court, Court.RIGHT_PADDLE, colors.RED)
ball = Ball(court, scorekeeper)

clock = pygame.time.Clock()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    left_score = scorekeeper.get_score(Scorekeeper.LEFT_PLAYER)
    right_score = scorekeeper.get_score(Scorekeeper.RIGHT_PLAYER)
    if left_score == WINNING_SCORE or right_score == WINNING_SCORE:
        state_manager.set_state(StateManager.GAME_OVER_STATE)

    if not done:
        screen.fill(colors.BLACK)

        keys = pygame.key.get_pressed()
        if state_manager.get_state() == StateManager.PLAYING_STATE:
            left_paddle.move(keys[pygame.K_w], keys[pygame.K_s])
            right_paddle.move(keys[pygame.K_UP], keys[pygame.K_DOWN])
        elif state_manager.get_state() == StateManager.GAME_OVER_STATE:
            if keys[pygame.K_SPACE]:
                scorekeeper.reset()
                left_paddle.reset()
                right_paddle.reset()
                state_manager.set_state(StateManager.GET_READY_STATE)

        state_manager.update()
        message_board.update()
        scoreboard.update()
        if state_manager.get_state() == StateManager.PLAYING_STATE:
            court.update()

        message_board.draw(screen)
        scoreboard.draw(screen)
        court.draw(screen)

        pygame.display.flip()
        clock.tick(FRAME_RATE)
   
pygame.quit()
