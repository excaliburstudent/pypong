import pygame
import colors

class Paddle:

    WIDTH = 10
    HEIGHT = 75
    
    def __init__(self, court, which):
        self.x = court.get_paddle_x(which) - Paddle.WIDTH // 2
        self.y = court.get_paddle_y() - Paddle.HEIGHT // 2
        court.add_object(self)

    def update(self, bounds):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, colors.WHITE, pygame.Rect(self.x, self.y, Paddle.WIDTH, Paddle.HEIGHT))