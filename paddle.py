import pygame
import colors

class Paddle:

    WIDTH = 10
    HEIGHT = 75
    
    UP = -1
    DOWN = 1
    NOT_MOVING = 0
    MOVE_AMOUNT = 3

    def __init__(self, court, which, color):
        self.initial_position = (court.get_paddle_x(which) - Paddle.WIDTH // 2, court.get_paddle_y() - Paddle.HEIGHT // 2)
        self.color = color
        self.reset()
        court.add_object(self)

    def reset(self):
        self.x, self.y = self.initial_position
        self.move_direction = Paddle.NOT_MOVING

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
    
    def is_touching(self, rect, h_direction, v_direction):
        top_edge = (self.x, self.y, self.x + Paddle.WIDTH, self.y)
        bottom_edge = (self.x, self.y + Paddle.HEIGHT, self.x + Paddle.WIDTH, self.y + Paddle.HEIGHT)
        if rect.clipline(top_edge) or rect.clipline(bottom_edge):
            return v_direction
        
        left_face = (self.x, self.y, self.x, self.y + Paddle.HEIGHT)
        right_face = (self.x + Paddle.WIDTH, self.y, self.x + Paddle.WIDTH, self.y + Paddle.HEIGHT)
        if rect.clipline(left_face) or rect.clipline(right_face):
            return h_direction
        
        return None
    
    def update(self, bounds):
        self.y += self.move_direction * Paddle.MOVE_AMOUNT
        if self.y < 0:
            self.y = 0
        elif self.y + Paddle.HEIGHT > bounds[1]:
            self.y = bounds[1] - Paddle.HEIGHT

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.get_rect())