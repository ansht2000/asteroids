import pygame
import pygame.gfxdraw
from powerup import Powerup
from player import Player

class SpeedPowerup(Powerup):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        a = self.position + pygame.Vector2(-10, 2)
        b = self.position + pygame.Vector2(5, -20)
        c = self.position + pygame.Vector2(2, -2)
        d = self.position + pygame.Vector2(10, -2)
        e = self.position + pygame.Vector2(-5, 20)
        f = self.position + pygame.Vector2(-2, 2)
        points = [a, b, c, d, e, f]
        pygame.gfxdraw.filled_polygon(screen, points, (204, 255, 0))

    def apply_powerup(self, player: Player):
        player.acceleration += 5
