import pygame
from constants import *

class TriangleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.points = []
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision_detected_with_circle_shape(self, other):
        lengths = []
        for point in self.points:
            lengths.append((point - other.position).length())
        min_len = min(lengths)
        return min_len <= other.radius