import pygame
import colors
from scorekeeper import *

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
        self.initialize_digits()

    def initialize_digits(self):
        self.digits = []
        for _ in range(0, 10):
            surface = pygame.Surface((Scoreboard.NUMBER_WIDTH, Scoreboard.NUMBER_HEIGHT))
            surface.fill(colors.WHITE)
            self.digits.append(surface)

        self.initialize_zero(self.digits[0])   
        self.initialize_one(self.digits[1]) 
        self.initialize_two(self.digits[2])
        self.initialize_three(self.digits[3])
        self.initialize_four(self.digits[4])
        self.initialize_five(self.digits[5])
        self.initialize_six(self.digits[6])
        self.initialize_seven(self.digits[7])
        self.initialize_eight(self.digits[8])
        self.initialize_nine(self.digits[9])

    def update(self):
        pass

    def draw(self, surface):
        self.surface.fill(colors.BLACK)

        surface.blit(self.surface, (self.x, self.y))

    def initialize_zero(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH, 3 * Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_one(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (0, 0, Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_HEIGHT))

    def initialize_two(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_three(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_four(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, 0,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 2))

        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH * 2))
        
    def initialize_five(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_six(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_seven(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH * 4))

    def initialize_eight(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_nine(self, surface):
        pygame.draw.rect(surface, colors.BLACK,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, colors.BLACK,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
