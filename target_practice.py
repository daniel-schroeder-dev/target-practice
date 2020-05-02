import sys

import pygame

from box import Box
from ship import Ship
from bullet import Bullet
from welcome_message import WelcomeMessage
from start_button import StartButton

def run():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Target Pratice')

    welcome_message = WelcomeMessage('Welcome to Target Practice!', screen)
    start_button = StartButton(screen)

    box = Box(screen)
    ship = Ship(screen)
    bullets = pygame.sprite.Group()

    game_playing = False

    while True:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_DOWN:
                    ship.move_down()
                elif event.key == pygame.K_UP:
                    ship.move_up()
                elif event.key == pygame.K_SPACE:
                    bullets.add(Bullet(ship))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    ship.move_down(False)
                elif event.key == pygame.K_UP:
                    ship.move_up(False)

        screen.fill((200, 200, 200))

        if game_playing:
            box.update()
            screen.fill(box.color, box.rect)

            ship.update()
            ship.draw()

            bullets.update()

            for bullet in bullets.copy():
                if bullet.rect.left < screen.get_rect().right:
                    screen.fill(bullet.color, bullet.rect)
                else:
                    bullets.remove(bullet)
        else:
            screen.blit(welcome_message.image, welcome_message.rect)
            start_button.draw()

        pygame.display.flip()

run()

