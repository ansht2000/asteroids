import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = 0
    lives = 3
    font = pygame.font.SysFont("Arial", 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(70, 20))
    lives_rect = score_text.get_rect(center=(70, 60))
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0x000)
        screen.blit(score_text, score_rect)
        screen.blit(lives_text, lives_rect)
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if player.collision_detected(asteroid):
                lives -= 1
                lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
                if lives == 0:
                    game_over_text = font.render(f"Score: {score}", True, (255, 255, 255))
                    game_over_rect = score_text.get_rect(center=(pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2))
                    screen.blit(game_over_text, game_over_rect)
                    return
                player.position.x = pygame.display.get_window_size()[0] / 2
                player.position.y = pygame.display.get_window_size()[1] / 2
            for shot in shots:
                if shot.collision_detected(asteroid):
                    shot.kill()
                    if asteroid.split():
                        score += 1
                        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()