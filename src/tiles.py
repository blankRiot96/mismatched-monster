import pygame
import pytmx

from src.shared import Shared


class TileMap:
    def __init__(self) -> None:
        self.shared = Shared()
        self.tilemap = pytmx.load_pygame("assets/tiled/map.tmx")
        self.tilesize = self.tilemap.tilewidth
        self.gen_surf()

    def gen_surf(self):
        self.surface = pygame.Surface(
            (self.tilemap.width * self.tilesize, self.tilemap.height * self.tilesize),
            pygame.SRCALPHA,
        )
        for layer in self.tilemap.layers:
            for x, y, image in layer.tiles():
                self.surface.blit(image, (self.tilesize * x, self.tilesize * y))

    def update(self):
        ...

    def draw(self):
        self.shared.screen.blit(self.surface, (0, 0))
