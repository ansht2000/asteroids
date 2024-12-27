import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_state = START_MENU

    while(1):
        if game_state == START_MENU:
            game_state = start_menu(screen)
        if game_state == GAME:
            game_state = game_loop(screen, clock, dt)
        if game_state == GAME_OVER:
            game_state = game_over(screen)

def render_text(font: pygame.font.Font, text, color, center_position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center_position)
    return text_surface, text_rect

def start_menu(screen):
    while(1):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 36)
        start_text, start_rect = render_text(font, "Start Game", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 50))
        quit_text, quit_rect = render_text(font, "Quit Game", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 + 50))
        screen.blit(start_text, start_rect)
        screen.blit(quit_text, quit_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  start_rect.collidepoint(event.pos):
                    return GAME
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def game_over(screen):
    while(1):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 36)
        retry_text, retry_rect = render_text(font, "Try Again", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 - 50))
        quit_text, quit_rect = render_text(font, "Quit to Main Menu", (255, 255, 255), (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2 + 50))
        screen.blit(retry_text, retry_rect)
        screen.blit(quit_text, quit_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return GAME  # Switch back to the game state
                if quit_rect.collidepoint(event.pos):
                    return START_MENU

def game_loop(screen, clock, dt):
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
    score_text, score_rect = render_text(font, f"Score: {score}", (255, 255, 255), (70, 20))
    lives_text, lives_rect = render_text(font, f"Lives: {lives}", (255, 255, 255), (70, 60))
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
                    return GAME_OVER
                player.position.x = pygame.display.get_window_size()[0] / 2
                player.position.y = pygame.display.get_window_size()[1] / 2
            for shot in shots:
                if shot.collision_detected(asteroid):
                    asteroid.explode(screen)
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