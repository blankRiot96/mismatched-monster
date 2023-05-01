import typing as t

import pygame
import pytmx

from src.shared import Shared


class TileMap:
    COLLISION_DEPTH = 2

    def __init__(self) -> None:
        self.shared = Shared()
        self.tilemap = pytmx.load_pygame("assets/tiled/map.tmx")
        self.tilesize = self.tilemap.tilewidth
        self.gen_surf()
        self.gen_tiles()

    def gen_tiles(self):
        self.tiles = []
        for nth_layer, layer in enumerate(self.tilemap.layers):
            prev_x, prev_y = -1, -1
            row = []
            for x, y, image in layer.tiles():
                if x > prev_x + 1:
                    row.extend([None] * (x - prev_x))
                    prev_x, prev_y = x, y
                    continue
                row.append(
                    pygame.Rect(
                        x * self.tilesize,
                        y * self.tilesize,
                        self.tilesize,
                        self.tilesize,
                    )
                )
                if y > prev_y:
                    self.tiles.append(row)
                    row = []
                prev_x, prev_y = x, y

            for row in self.tiles:
                print(len(row))
                # for tile in row:
                # if tile is None:
                # print(0, end="")
                # else:
                # print(1, end="")
                # print()
            # row = []
            # for x in range(self.tilemap.width):
            #     for y in range(self.tilemap.height):
            #         tile = self.tilemap.get_tile_properties(x, y, nth_layer)
            #         if tile is None:
            #             row.append(None)
            #             continue

            #         rect = pygame.Rect(
            #             x * self.tilesize,
            #             y * self.tilesize,
            #             self.tilesize,
            #             self.tilesize,
            #         )
            #         row.append(rect)
            # self.tiles.append(row)

    def gen_surf(self):
        self.surface = pygame.Surface(
            (self.tilemap.width * self.tilesize, self.tilemap.height * self.tilesize),
            pygame.SRCALPHA,
        )
        for layer in self.tilemap.layers:
            for x, y, image in layer.tiles():
                self.surface.blit(image, (self.tilesize * x, self.tilesize * y))

    def get_tile(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.tiles[self.shared.player.grid_pos[0] + x][
                self.shared.player.grid_pos[1] + y
            ]
        except IndexError:
            return None

    def get_neighbouring_tiles(self) -> t.Iterator:
        for x in range(-self.COLLISION_DEPTH, self.COLLISION_DEPTH + 1):
            for y in range(-self.COLLISION_DEPTH, self.COLLISION_DEPTH + 1):
                tile = self.get_tile(x, y)
                if tile is None:
                    continue
                yield tile

    def update(self):
        self.near_tiles = tuple(self.get_neighbouring_tiles())

    def draw(self):
        self.shared.screen.blit(self.surface, self.shared.cam.transform((0, 0)))
        for tile in self.near_tiles:
            pygame.draw.rect(
                self.shared.screen,
                "red",
                (self.shared.cam.transform(tile), tile.size),
                1,
            )
