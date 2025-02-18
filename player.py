import pygame
import pygame.gfxdraw
from triangleshape import TriangleShape
from constants import *
from shot import Shot

class Player(TriangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        # integers 0-n represent different shot types
        # 0: single shot
        # 1: triple shot
        self.shot_type = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        side = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - side
        c = self.position - forward * self.radius * .5
        d = self.position - forward * self.radius + side
        self.points = [a, b, c, d]
        return self.points
    
    def draw(self, screen):
        triangle: list = self.triangle()
        pygame.gfxdraw.filled_polygon(screen, triangle, (255, 255, 255))
        pygame.draw.polygon(screen, "black", triangle, 2)

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
        match self.shot_type:
            case 0:
                self.shoot_timer = PLAYER_SINGLE_SHOOT_COOLDOWN
                shot = Shot(self.position.x, self.position.y)
                shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation)
                shot.velocity = shot_velocity * PLAYER_SHOOT_SPEED
            case 1:
                self.shoot_timer = PLAYER_TRIPLE_SHOOT_COOLDOWN
                shot_one = Shot(self.position.x, self.position.y)
                shot_two = Shot(self.position.x, self.position.y)
                shot_three = Shot(self.position.x, self.position.y)
                shot_one.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
                shot_two.velocity =  pygame.Vector2(0, 1).rotate(self.rotation - 30) * PLAYER_SHOOT_SPEED
                shot_three.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 30) * PLAYER_SHOOT_SPEED

    def apply_powerup(self):
        print("powerup applied")