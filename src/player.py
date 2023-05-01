import pygame

from src.shared import Shared


class Player:
    def __init__(self) -> None:
        self.image = pygame.image.load("assets/body.png").convert_alpha()
        self.shared = Shared()
        self.pos = pygame.Vector2(32 * 4, 32)
        self.rect = self.image.get_bounding_rect()
        self.rect.topleft = self.pos
        self.vel = pygame.Vector2(0, 100)
        self.dv = pygame.Vector2()
        self.gen_grid_pos()

    def gen_grid_pos(self):
        self.grid_pos = (int(self.pos.x / 32), int(self.pos.y / 32))

    def on_collision(self, tile: pygame.Rect):
        if self.pos.y > tile.y:
            print("step 2")
            self.dv.y = 0

    def handle_wallcollision(self):
        for tile in self.shared.tilemap.near_tiles:
            if self.rect.move(self.dv).colliderect(tile):
                print("step 1")
                self.on_collision(tile)

    def get_potential_movement(self):
        self.dv = self.vel * self.shared.dt

    def update(self):
        self.get_potential_movement()
        self.handle_wallcollision()
        self.pos += self.dv
        self.rect.topleft = self.pos
        self.gen_grid_pos()

    def draw(self):
        self.shared.screen.blit(self.image, self.shared.cam.transform(self.rect))
