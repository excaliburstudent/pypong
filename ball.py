import pygame
import random
import math
import colors

class Ball:

    SIZE = 5
    INITIAL_SPEED = 5
    MAX_ANGLE = 60
    MIN_ANGLE = -MAX_ANGLE

    def __init__(self, court):
        self.size = Ball.SIZE
        self.initial_position = court.get_center()
        court.set_ball(self)
        self.initialize_ball()

    def initialize_ball(self):
        self.position = self.initial_position
        angle = math.radians(random.randint(Ball.MIN_ANGLE, Ball.MAX_ANGLE) + random.choice([0, 180]))
        self.delta_x = math.cos(angle)
        self.delta_y = math.sin(angle)
        self.speed = Ball.INITIAL_SPEED

    def update(self, bounds):
        new_x = self.get_new_x()
        new_y = self.get_new_y()
        self.position = (new_x, new_y)

    def get_new_x(self):
        return self.position[0] + self.speed * self.delta_x
    
    def get_new_y(self):
        return self.position[1] + self.speed * self.delta_y

    def draw(self, surface):
        pygame.draw.circle(surface, colors.WHITE, self.position, self.size)