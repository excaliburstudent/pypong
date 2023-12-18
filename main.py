import pygame
import time
from court import *
from paddle import *
from ball import *
from scorekeeper import *
from scoreboard import *

BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600
SCOREBOARD_HEIGHT = 100
BOTTOM_PANEL_HEIGHT = 50
FRAME_RATE = 30
WINNING_SCORE = 9

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
scorekeeper = Scorekeeper()
scoreboard = Scoreboard(scorekeeper, 0, 0, WIDTH, SCOREBOARD_HEIGHT)
court = Court(0, SCOREBOARD_HEIGHT, WIDTH, HEIGHT - SCOREBOARD_HEIGHT - BOTTOM_PANEL_HEIGHT)
left_paddle = Paddle(court, Court.LEFT_PADDLE)
right_paddle = Paddle(court, Court.RIGHT_PADDLE)
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
        pygame.mixer.Sound("assets/sounds/mixkit-arcade-retro-game-over-213.wav").play()
        time.sleep(2)
        done = True

    if not done:
        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        left_paddle.move(keys[pygame.K_w], keys[pygame.K_s])
        right_paddle.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

        scoreboard.update()
        court.update()

        scoreboard.draw(screen)
        court.draw(screen)

        pygame.display.flip()
        clock.tick(FRAME_RATE)
   
pygame.quit()
