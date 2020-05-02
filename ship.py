import pygame

class Ship(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load('./ship.png')
        self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.centery = screen.get_rect().centery
        self.rect.left = 0

        self.moving_down = False
        self.moving_up = False

        self.speed = 8

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self, should_move=True):
        self.moving_up = should_move

    def move_down(self, should_move=True):
        self.moving_down = should_move

    def is_touching_bottom_screen(self):
        return self.rect.bottom >= self.screen.get_rect().bottom

    def is_touching_top_screen(self):
        return self.rect.top <= 0

    def reset(self):
        self.rect.centery = self.screen.get_rect().centery
        self.rect.left = 0

        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_down and not self.is_touching_bottom_screen():
            self.rect.y += self.speed
        if self.moving_up and not self.is_touching_top_screen():
            self.rect.y -= self.speed

