import pygame
from court import *
from paddle import *
from ball import *

BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600
SCOREBOARD_HEIGHT = 100
BOTTOM_PANEL_HEIGHT = 50
FRAME_RATE = 30

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
court = Court(0, SCOREBOARD_HEIGHT, WIDTH, HEIGHT - SCOREBOARD_HEIGHT - BOTTOM_PANEL_HEIGHT)
left_paddle = Paddle(court, Court.LEFT_PADDLE)
right_paddle = Paddle(court, Court.RIGHT_PADDLE)
ball = Ball(court)

clock = pygame.time.Clock()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        left_paddle.move(keys[pygame.K_w], keys[pygame.K_s])
        right_paddle.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

        court.update()

        court.draw(screen)

        pygame.display.flip()
        clock.tick(FRAME_RATE)
   
pygame.quit()
