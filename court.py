import pygame
import colors

class Court:

    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top

    def update(self):
        pass

    def draw(self, surface):
        self.surface.fill(colors.BLACK)
        right = self.surface.get_width() - 1
        bottom = self.surface.get_height() - 1
        pygame.draw.line(self.surface, colors.WHITE, (0, 0), (right, 0))
        pygame.draw.line(self.surface, colors.WHITE, (0, bottom), (right, bottom))

        self.draw_net()

        surface.blit(self.surface, (self.x, self.y))

    def draw_net(self):
        pos = 0
        center = self.surface.get_rect().centerx
        pen_down = False
        while pos < self.surface.get_height():
            if pen_down:
                pygame.draw.line(self.surface, colors.WHITE, (center, pos), (center, pos + 10))
            pos += 10
            pen_down = not pen_down