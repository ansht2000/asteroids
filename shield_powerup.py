import pygame
import pygame.gfxdraw
from powerup import Powerup
from player import Player

class ShieldPowerup(Powerup):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), 20, (78, 142, 245))
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), 15, (152, 157, 163))
        pygame.gfxdraw.filled_circle(screen, int(self.position.x), int(self.position.y), 4, (78, 142, 245))

    def apply_powerup(self, player: Player):
        player.shield = True