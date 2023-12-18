import pygame
import colors

class MessageBoard:

    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top
        self.font = pygame.font.SysFont(None, 24)
        self.message = "I am the message board"

    def update(self):
        pass

    def draw(self, surface):
        self.surface.fill(colors.BLACK)

        message_text = self.font.render(self.message, True, colors.WHITE)
        message_rect = message_text.get_rect()
        message_rect.center = self.surface.get_rect().center
        self.surface.blit(message_text, message_rect)

        surface.blit(self.surface, (self.x, self.y))
