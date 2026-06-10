import pygame


class Scrollbar:
    def __init__(self, bg_rectangle: pygame.Rect, thumb_width: int, thumb_height: int):
        """
        Initialize a reusable vertical scrollbar component.
        :param bg_rectangle: pygame.Rect() defining the track position and size.
        :param thumb_width: Width of draggable slider handle.
        :param thumb_height: Height of draggable slider handle.
        """
        # Track geometry
        self.track_rect = bg_rectangle

        # Build thumb rectangle centered horizontally on the track
        thumb_x = self.track_rect.x + (self.track_rect.width - thumb_width) // 2
        thumb_y = self.track_rect.y
        self.thumb_rect = pygame.Rect(thumb_x, thumb_y, thumb_width, thumb_height)

        # State tracking flags
        self.is_dragging = False
        self.mouse_offset_y = 0
        self.scroll_value = 0.0  # Output float between 0.0 and 1.0

    def handle_event(self, event: pygame.event.Event):
        """Process mouse interactions."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.thumb_rect.collidepoint(event.pos):
                self.is_dragging = True
                # Store distance from click spot to top of thumb
                self.mouse_offset_y = self.thumb_rect.y - event.pos[1]

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False

    def update(self):
        """Calculate sliding positions and clamps values when dragging."""
        if self.is_dragging:
            mouse_y = pygame.mouse.get_pos()[1]
            new_y = mouse_y + self.mouse_offset_y

            # Clamp boundaries inside the track constraints
            min_y = self.track_rect.top
            max_y = self.track_rect.bottom - self.thumb_rect.height
            self.thumb_rect.y = max(min_y, min(new_y, max_y))

            # Recompute current percentage from 0.0 to 1.0
            total_travel = self.track_rect.height - self.thumb_rect.height
            if total_travel > 0:
                current_travel = self.thumb_rect.y - self.track_rect.top
                self.scroll_value = current_travel / total_travel
            else:
                self.scroll_value = 0.0

    def draw(self, surface: pygame.Surface, track_color="gray20", thumb_color="gray70"):
        """Draw the track and slider on the specified target surface canvas."""
        pygame.draw.rect(surface, track_color, self.track_rect, border_radius=5)
        pygame.draw.rect(surface, thumb_color, self.thumb_rect, border_radius=5)
