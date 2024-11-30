import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt): 
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, accelerating, decelerating):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        if accelerating:
            self.velocity += direction * PLAYER_ACCELERATION * dt
        elif decelerating:
            self.velocity -= direction * PLAYER_ACCELERATION * dt
        self.position += self.velocity * dt
        self.position.x %= pygame.display.get_window_size()[0]
        self.position.y %= pygame.display.get_window_size()[1]

    def update(self, dt):
        accelerating = False
        decelerating = False
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            accelerating = True
        if keys[pygame.K_s]:
            decelerating = True
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.move(dt, accelerating, decelerating)
        self.velocity *= DAMPING_FACTOR

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot_speed = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = shot_speed * PLAYER_SHOOT_SPEED