import pygame
import src.constants

border_color = src.constants.CYLINDER_BORDER_COLOR
border_rect = pygame.Rect(50, 50, 0, 100)
border_width = 2


def drawCylinder(surface) -> None:
    pygame.draw.rect(
        surface,
        src.cylinder.border_color,
        src.cylinder.border_rect,
        src.cylinder.border_width
    )
