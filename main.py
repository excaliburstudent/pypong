import pygame

BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not done:
        screen.fill(BLACK)

pygame.quit()
