from src.state_enums import State
from src.tiles import TileMap


class GameState:
    def __init__(self) -> None:
        self.next_state: State | None = None
        self.tilemap = TileMap()

    def update(self):
        self.tilemap.update()

    def draw(self):
        self.tilemap.draw()
