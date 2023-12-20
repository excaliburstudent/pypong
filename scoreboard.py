import pygame
import colors
from scorekeeper import *

class Scoreboard:

    BACKGROUND_COLOR = colors.GRAY
    TOP_MARGIN = 20
    SIDE_MARGIN = 50
    NUMBER_STROKE_WIDTH = 10
    NUMBER_WIDTH = 3 * NUMBER_STROKE_WIDTH
    NUMBER_HEIGHT = 5 * NUMBER_STROKE_WIDTH

    def __init__(self, scorekeeper, left, top, width, height, left_color, right_color):
        self.x = left
        self.y = top
        self.surface = pygame.Surface((width, height))
        self.scorekeeper = scorekeeper
        self.left_color = left_color
        self.right_color = right_color
        self.initialize_digits()

    def initialize_digits(self):
        self.digits = []
        for _ in range(0, 10):
            surface = pygame.Surface((Scoreboard.NUMBER_WIDTH, Scoreboard.NUMBER_HEIGHT))
            surface.fill(colors.WHITE)
            surface.set_colorkey(colors.WHITE)
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
        self.surface.fill(Scoreboard.BACKGROUND_COLOR)

        left_score = self.scorekeeper.get_score(Scorekeeper.LEFT_PLAYER)
        left_surface = pygame.Surface((Scoreboard.NUMBER_WIDTH, Scoreboard.NUMBER_HEIGHT))
        left_surface.fill(self.left_color)
        left_surface.blit(self.digits[left_score], (0, 0))

        right_score = self.scorekeeper.get_score(Scorekeeper.RIGHT_PLAYER)
        right_surface = pygame.Surface((Scoreboard.NUMBER_WIDTH, Scoreboard.NUMBER_HEIGHT))
        right_surface.fill(self.right_color)
        right_surface.blit(self.digits[right_score], (0, 0))

        self.surface.blit(left_surface, (self.x + Scoreboard.SIDE_MARGIN, self.y + Scoreboard.TOP_MARGIN))
        self.surface.blit(right_surface, (self.surface.get_width() - Scoreboard.SIDE_MARGIN - Scoreboard.NUMBER_WIDTH,
                                                     self.y + Scoreboard.TOP_MARGIN))
        
        surface.blit(self.surface, (self.x, self.y))

    def initialize_zero(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH, 3 * Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_one(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, 0, Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_HEIGHT))

    def initialize_two(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_three(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
        
    def initialize_four(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, 0,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 2))

        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH * 2))
        
    def initialize_five(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_six(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_seven(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH * 4))

    def initialize_eight(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

    def initialize_nine(self, surface):
        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH,
                          Scoreboard.NUMBER_STROKE_WIDTH, Scoreboard.NUMBER_STROKE_WIDTH))

        pygame.draw.rect(surface, Scoreboard.BACKGROUND_COLOR,
                         (0, Scoreboard.NUMBER_STROKE_WIDTH * 3,
                          Scoreboard.NUMBER_STROKE_WIDTH * 2, Scoreboard.NUMBER_STROKE_WIDTH))
