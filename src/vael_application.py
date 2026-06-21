import pygame
import ui.cylinder_volume_scrollbar
import sys

import src.constants
import src.cylinder


class VaelApplication:
    window = 0

    def __init__(self):
        pygame.init()
        self._initWindow()
        self._initFont()

    def run(self):
        self._mainApplicationLoop()

    def destroy(self):
        pygame.quit()
        sys.exit()

    def _initWindow(self):
        self.window = pygame.display.set_mode(
            (
                src.constants.INITIAL_WINDOW_WIDTH,
                src.constants.INITIAL_WINDOW_HEIGHT
            ),
            pygame.RESIZABLE
        )
        pygame.display.set_caption(src.constants.WINDOW_CAPTION)

    def _initFont(self):
        self.font = pygame.font.SysFont(
            src.constants.FONT_FAMILY,
            src.constants.FONT_SIZE
        )

    def _mainApplicationLoop(self) -> None:
        clock = pygame.time.Clock()
        running = True

        # Main loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                ui.cylinder_volume_scrollbar.scrollbar.handle_event(event)

            # Updates
            ui.cylinder_volume_scrollbar.scrollbar.update()
            if ui.cylinder_volume_scrollbar.scrollbar.scroll_value == 0:
                src.cylinder.border_rect.width = ui.cylinder_volume_scrollbar.scrollbar.scroll_value * 250 + src.constants.MINIMUM_CYLINDER_WIDTH
            else:
                src.cylinder.border_rect.width = ui.cylinder_volume_scrollbar.scrollbar.scroll_value * 250

            text_surface = self.font.render("Cylinder Volume", True, src.constants.WHITE)

            self.window.fill(src.constants.BLACK)

            src.cylinder.drawCylinder(self.window)
            self.window.blit(text_surface, (800, 20))
            ui.cylinder_volume_scrollbar.scrollbar.draw(self.window)

            pygame.display.flip()
            clock.tick(60)
