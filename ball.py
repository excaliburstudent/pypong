import pygame
import colors

class Ball:

    SIZE = 5

    def __init__(self, court):
        self.size = Ball.SIZE
        self.initial_position = court.get_center()
        court.set_ball(self)
        self.initialize_ball()

    def initialize_ball(self):
        self.position = self.initial_position

    def update(self, bounds):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, colors.WHITE, self.position, self.size)