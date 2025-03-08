import pygame
import pygame.gfxdraw
from circleshape import CircleShape

class Powerup(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pass

    def update(self, dt):
        self.position += self.velocity * dt

    def apply_powerup(self, player):
        pass

    