import pygame

class StartButton:

    def __init__(self, screen):
        self.width = 150
        self.height = 75
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = screen.get_rect().center
        self.color = (48, 145, 74)
