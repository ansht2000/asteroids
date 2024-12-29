import pygame

def render_text(font: pygame.font.Font, text, color, center_position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center_position)
    return text_surface, text_rect