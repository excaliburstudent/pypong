import pygame
import random
import math
import colors

class Ball:

    HORIZONTAL = -1
    VERTICAL = 1
    BOUNCE_VARIANCE = 0.2
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
        if new_x < 0 or new_x > bounds[0]:
            self.bounce(Ball.HORIZONTAL)
            new_x = self.get_new_x()

        new_y = self.get_new_y()
        if new_y - self.size < 0 or new_y + self.size > bounds[1]:
            self.bounce(Ball.VERTICAL)
            new_y = self.get_new_y()

        self.position = (new_x, new_y)

    def bounce(self, direction):
        if direction == Ball.HORIZONTAL:
            self.delta_x = -self.delta_x
            self.delta_y += random.random() * Ball.BOUNCE_VARIANCE * random.choice([1, -1])
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y
            self.delta_x += random.random() * Ball.BOUNCE_VARIANCE * random.choice([1, -1])

    def get_new_x(self):
        return self.position[0] + self.speed * self.delta_x
    
    def get_new_y(self):
        return self.position[1] + self.speed * self.delta_y

    def draw(self, surface):
        pygame.draw.circle(surface, colors.WHITE, self.position, self.size)