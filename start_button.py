import pygame

class StartButton:

    def __init__(self, screen):
        self.screen = screen

        self.width = 150
        self.height = 75
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = screen.get_rect().center
        self.color = (48, 145, 74)

        font = pygame.font.SysFont(None, 38)
        font_color = (0, 0, 0)
        self.text = font.render('Start', True, font_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text, self.text_rect)

