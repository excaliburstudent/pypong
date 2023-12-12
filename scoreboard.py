import pygame
import colors

class Scoreboard:

    TOP_MARGIN = 20
    SIDE_MARGIN = 50
    NUMBER_STROKE_WIDTH = 10
    NUMBER_WIDTH = 3 * NUMBER_STROKE_WIDTH
    NUMBER_HEIGHT = 5 * NUMBER_STROKE_WIDTH

    def __init__(self, scorekeeper, left, top, width, height):
        self.x = left
        self.y = top
        self.surface = pygame.Surface((width, height))
        self.scorekeeper = scorekeeper

    def update(self):
        pass

    def draw(self, surface):
        self.surface.fill(colors.BLACK)