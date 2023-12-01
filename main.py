import pygame
from court import *
from paddle import *

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
paddle1 = Paddle(court, Court.LEFT_PADDLE)
paddle2 = Paddle(court, Court.RIGHT_PADDLE)

clock = pygame.time.Clock()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(BLACK)

        court.update()

        court.draw(screen)

        pygame.display.flip()
        clock.tick(FRAME_RATE)
   
pygame.quit()
