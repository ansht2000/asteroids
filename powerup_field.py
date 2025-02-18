import pygame
import random
from powerup import Powerup
from constants import *

class PowerupField(pygame.sprite.Sprite):
    spawn_edge = [pygame.Vector2(0, 1), lambda x: pygame.Vector2(x * pygame.display.get_window_size()[0], 0)]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        powerup = Powerup(position.x, position.y, radius)
        powerup.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE:
            self.spawn_timer = 0
            velocity = self.spawn_edge[0] * POWERUP_SPEED
            position = self.spawn_edge[1](random.uniform(0, 1))
            self.spawn(40, position, velocity)