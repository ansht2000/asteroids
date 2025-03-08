import pygame
import random
from shield_powerup import ShieldPowerup
from speed_powerup import SpeedPowerup
from constants import *

class PowerupField(pygame.sprite.Sprite):
    spawn_edge = [pygame.Vector2(0, 1), lambda x: pygame.Vector2(x * pygame.display.get_window_size()[0], 0)]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        powerup_type = random.randint(0, 1)
        if powerup_type:
            powerup = SpeedPowerup(position.x, position.y, radius)
        else:
            powerup = ShieldPowerup(position.x, position.y, radius)
        powerup.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE:
            self.spawn_timer = 0
            velocity = self.spawn_edge[0] * POWERUP_SPEED
            position = self.spawn_edge[1](random.uniform(0, 1))
            self.spawn(20, position, velocity)