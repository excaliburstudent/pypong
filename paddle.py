import pygame
import colors

class Paddle:

    WIDTH = 10
    HEIGHT = 75
    
    UP = -1
    DOWN = 1
    NOT_MOVING = 0
    MOVE_AMOUNT = 3

    def __init__(self, court, which):
        self.x = court.get_paddle_x(which) - Paddle.WIDTH // 2
        self.y = court.get_paddle_y() - Paddle.HEIGHT // 2
        self.move_direction = Paddle.NOT_MOVING
        court.add_object(self)

    def move(self, up, down):
        if up and down:
            self.move_direction = Paddle.NOT_MOVING
        elif up:
            self.move_direction = Paddle.UP
        elif down:
            self.move_direction = Paddle.DOWN
        else:
            self.move_direction = Paddle.NOT_MOVING

    def get_rect(self):
        return pygame.Rect(self.x, self.y, Paddle.WIDTH, Paddle.HEIGHT)
    
    def update(self, bounds):
        self.y += self.move_direction * Paddle.MOVE_AMOUNT
        if self.y < 0:
            self.y = 0
        elif self.y + Paddle.HEIGHT > bounds[1]:
            self.y = bounds[1] - Paddle.HEIGHT

    def draw(self, surface):
        pygame.draw.rect(surface, colors.WHITE, self.get_rect())