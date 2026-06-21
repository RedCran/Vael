import pygame
import ui.Components.Scrollbar

# Variables
scrollbar_bgrect_posx = 870
scrollbar_bgrect_posy = 50
scrollbar_bgrect_width = 10
scrollbar_bgrect_height = 100

scrollbar_bgrect = pygame.Rect(
    scrollbar_bgrect_posx,
    scrollbar_bgrect_posy,
    scrollbar_bgrect_width,
    scrollbar_bgrect_height
)

scrollbar = ui.Components.Scrollbar.Scrollbar(scrollbar_bgrect, 10, 10)
