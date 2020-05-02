import pygame

class WelcomeMessage:

    def __init__(self, message, screen):
        self.font = pygame.font.SysFont(None, 48)
        self.color = (0, 0, 0)
        self.image = self.font.render(message, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.centery = screen.get_rect().centery - 100
