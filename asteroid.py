import pygame
import random

import pygame.gfxdraw
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
        new_angle = random.uniform(0, 360)
        new_aster_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster_1 = Asteroid(self.position.x, self.position.y, new_aster_radius)
        new_aster_2 = Asteroid(self.position.x, self.position.y, new_aster_radius)
        new_aster_1.velocity = 1.2 * self.velocity.rotate(new_angle)
        new_aster_2.velocity = 1.2 * self.velocity.rotate(-new_angle)
    
    def explode(self, screen):
        particles = []
        for _ in range(30):
            rand_x = random.uniform(self.position.x - self.radius, self.position.x + self.radius)
            rand_y = random.uniform(self.position.y - self.radius, self.position.y + self.radius)
            particles.append((rand_x, rand_y))
        for particle in particles:
            pygame.gfxdraw.pixel(screen, int(particle[0]) - 1, int(particle[1]), (255, 255, 255))
            pygame.gfxdraw.pixel(screen, int(particle[0]), int(particle[1]), (255, 255, 255))
            pygame.gfxdraw.pixel(screen, int(particle[0]), int(particle[1]) + 1, (255, 255, 255))
            pygame.gfxdraw.pixel(screen, int(particle[0]) - 1, int(particle[1]) + 1, (255, 255, 255))

