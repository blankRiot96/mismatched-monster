from src.camera import Camera
from src.player import Player
from src.shared import Shared
from src.state_enums import State
from src.tiles import TileMap


class GameState:
    def __init__(self) -> None:
        self.shared = Shared()
        self.next_state: State | None = None
        self.shared.tilemap = TileMap()
        self.shared.player = Player()
        self.shared.cam = Camera()

    def update(self):
        self.shared.tilemap.update()
        self.shared.player.update()
        self.shared.cam.attach_to_player()

    def draw(self):
        self.shared.tilemap.draw()
        self.shared.player.draw()
