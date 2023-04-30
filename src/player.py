import pygame

import utils


class Player:
    def __init__(self) -> None:
        self.image = pygame.image.load("assets/body.png").convert_alpha()
        self.rect = self.image.get_rect()
