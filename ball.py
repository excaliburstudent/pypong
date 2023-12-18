import pygame
import random
import math
import colors
from scorekeeper import *

class Ball:

    HORIZONTAL = -1
    VERTICAL = 1
    BOUNCE_VARIANCE = 0.2
    SIZE = 5
    INITIAL_SPEED = 5
    MAX_ANGLE = 60
    MIN_ANGLE = -MAX_ANGLE

    def __init__(self, court, scorekeeper):
        self.size = Ball.SIZE
        self.scorekeeper = scorekeeper
        self.initial_position = court.get_center()
        self.bounce_sound = pygame.mixer.Sound("assets/sounds/4359__noisecollector__pongblipf4.wav")
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
        if new_x < 0:
            print("Point for right player")
            self.scorekeeper.award_point(Scorekeeper.RIGHT_PLAYER)
            self.initialize_ball()
            return

        if new_x > bounds[0]:
            print("Point for left player")
            self.scorekeeper.award_point(Scorekeeper.LEFT_PLAYER)
            self.initialize_ball()
            return
        
        new_y = self.get_new_y()
        if new_y - self.size < 0 or new_y + self.size > bounds[1]:
            self.bounce(Ball.VERTICAL)
            new_y = self.get_new_y()

        self.position = (new_x, new_y)

    def bounce(self, direction):
        self.bounce_sound.play()
        if direction == Ball.HORIZONTAL:
            self.delta_x = -self.delta_x
            self.delta_y += random.random() * Ball.BOUNCE_VARIANCE * random.choice([1, -1])
        elif direction == Ball.VERTICAL:
            self.delta_y = -self.delta_y
            self.delta_x += random.random() * Ball.BOUNCE_VARIANCE * random.choice([1, -1])

    def check_for_contact(self, objects):
        center_x, center_y = self.position
        diameter = 2 * self.size
        ball_rect = pygame.Rect(center_x - self.size, center_y - self.size, diameter, diameter)
        for object in objects:
            if object != self and ball_rect.colliderect(object.get_rect()):
                self.bounce(Ball.HORIZONTAL)
                break

    def get_new_x(self):
        return self.position[0] + self.speed * self.delta_x
    
    def get_new_y(self):
        return self.position[1] + self.speed * self.delta_y

    def draw(self, surface):
        pygame.draw.circle(surface, colors.WHITE, self.position, self.size)