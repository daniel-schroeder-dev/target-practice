import sys

import pygame

from box import Box
from ship import Ship

def run():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Target Pratice')

    box = Box(screen)
    ship = Ship(screen)

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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    ship.move_down(False)
                elif event.key == pygame.K_UP:
                    ship.move_up(False)

        screen.fill((200, 200, 200))
        box.update()
        screen.fill(box.color, box.rect)
        ship.update()
        ship.draw()
        pygame.display.flip()

run()

