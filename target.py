import pygame

class Target(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.width = 50
        self.height = 100
        self.color = (255, 0, 0)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.top = 0
        self.rect.right = screen.get_rect().right

        self.moving_down = True
        self.speed = 5

    def reset(self):
        self.rect.top = 0
        self.rect.right = self.screen.get_rect().right
        self.moving_down = True

    def update(self):
        if not self.moving_down and self.rect.top < 0:
            self.moving_down = True
        elif self.rect.bottom >= self.screen.get_rect().bottom:
            self.moving_down = False

        if self.moving_down:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

