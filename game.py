import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from render_utils import render_text

class Game:
    def __init__(self, screen, clock, dt):
        self.screen = screen
        self.clock = clock
        self.dt = dt
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        Player.containers = (self.drawable, self.updatable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.shots, self.updatable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()
        self.score = 0
        self.lives = 3
        self.font = pygame.font.SysFont("Arial", 36)
        score_text, score_rect = render_text(
            self.font,
            f"Score: {self.score}",
            (255, 255, 255),
            (70, 20)
        )
        lives_text, lives_rect = render_text(
            self.font,
            f"Lives: {self.lives}",
            (255, 255, 255),
            (70, 60)
        )
        self.score_text = score_text
        self.score_rect = score_rect
        self.lives_text = lives_text
        self.lives_rect = lives_rect

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.player.shot_type += 1
                        self.player.shot_type %= 2
            self.screen.fill(0x000)
            self.screen.blit(self.score_text, self.score_rect)
            self.screen.blit(self.lives_text, self.lives_rect)
            for object in self.updatable:
                object.update(self.dt)
            for asteroid in self.asteroids:
                if self.player.collision_detected(asteroid):
                    self.lives -= 1
                    self.lives_text = self.font.render(
                        f"Lives: {self.lives}",
                        True,
                        (255, 255, 255)
                    )
                    if self.lives <= 0:
                        return GAME_OVER
                    self.player.position.x = pygame.display.get_window_size()[0] / 2
                    self.player.position.y = pygame.display.get_window_size()[1] / 2
                for shot in self.shots:
                    if shot.collision_detected(asteroid):
                        asteroid.explode(self.screen)
                        shot.kill()
                        if asteroid.split():
                            self.score += 10
                            self.score_text = self.font.render(
                                f"Score: {self.score}",
                                True,
                                (255, 255, 255)
                            )
            for object in self.drawable:
                object.draw(self.screen)
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
            print(self.clock.get_fps())


