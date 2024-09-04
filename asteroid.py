import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return True
        new_angle = random.uniform(20, 50)
        new_aster_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster_1 = Asteroid(self.position.x, self.position.y, new_aster_radius)
        new_aster_2 = Asteroid(self.position.x, self.position.y, new_aster_radius)
        new_aster_1.velocity = 1.2 * self.velocity.rotate(new_angle)
        new_aster_2.velocity = 1.2 * self.velocity.rotate(-new_angle)

