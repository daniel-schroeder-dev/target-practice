import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, ship, *groups):
        super().__init__(*groups)

        self.color = (60, 60, 60)
        self.width = 10
        self.height = 4

        self.left = ship.rect.right
        self.top = ship.rect.centery - (self.height / 2)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

        self.velocity = 10

    def update(self):
        self.rect.x += self.velocity
