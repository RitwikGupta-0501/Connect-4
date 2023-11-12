import pygame


class Coin:
    """
    A Class of the player coin.
    """

    def __init__(self, left_boundary, right_boundary, posx, radius, colour):
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.posx = posx
        self.radius = radius
        self.colour = colour

    # Draws movable cursor on screen
    def draw_cursor(self, screen, square_size):
        if self.posx - self.radius // 2 <= self.left_boundary:
            self.posx = self.left_boundary + self.radius // 2
        elif self.posx + self.radius // 2 >= self.right_boundary:
            self.posx = self.right_boundary - self.radius // 2

        col = self.posx // square_size
        pos_X = (col * square_size) + square_size // 2

        pygame.draw.circle(screen, self.colour, (pos_X + 3.95, square_size // 2 + 4), self.radius)

    # Draws the Coin on Screen
    def draw_coin(self, screen, center, radius):
        pygame.draw.circle(screen, self.colour, center, radius)


class Button:
    """
    a CLass of Button Objects
    """

    def __init__(self, x, y, text_height, padding, inactive_colour, active_colour, function,
                 text="Button"):
        self.font = pygame.font.SysFont("Segeo UI", text_height)
        self.x = x
        self.y = y
        self.text = self.font.render(text, True, (255, 255, 255))

        self.height = self.text.get_height() + padding
        self.width = self.text.get_width() + padding
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.func = function

    def draw_button(self, screen, mouse_pos_x, mouse_pos_y):

        text_center_pos = (self.width // 2) + self.x, (self.height // 2) + self.y

        if self.rect.collidepoint(mouse_pos_x, mouse_pos_y):
            pygame.draw.rect(screen, self.active_colour, self.rect, border_radius=10)
        else:
            pygame.draw.rect(screen, self.inactive_colour, self.rect, border_radius=13)
        screen.blit(self.text, (self.text.get_rect(center=text_center_pos)))

    def click(self, param=None):
        if param is None:
            return self.func()
        else:
            return self.func(param)

    def collided(self, x, y):
        return self.rect.collidepoint(x, y)


class TextBox:
    """
    A Textbox Class
    """

    def __init__(self, x: int, y: int, text_height: int, padding: int, length: int, inactive_colour: tuple,
                 active_colour: tuple, filled_colour, border_thickness: int, default_text: str):
        self.x = x
        self.y = y
        self.padding = padding
        self.text_height = text_height
        self.length = length
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour
        self.filled_colour = filled_colour
        self.border_thickness = border_thickness
        self.rect = pygame.Rect(self.x, self.y, self.length, self.text_height + self.padding)
        self.active = False
        self.filled = False
        self.text = default_text
        self.default = default_text
        self.font = pygame.font.SysFont("Segeo UI", self.text_height)

    def draw_box(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.active_colour, self.rect, width=self.border_thickness)
        elif self.filled:
            pygame.draw.rect(screen, self.filled_colour, self.rect, width=self.border_thickness)
        else:
            pygame.draw.rect(screen, self.inactive_colour, self.rect, width=self.border_thickness)

    def render_text(self, screen):
        display_text = self.font.render(self.text, True, (255, 255, 255))
        text_pos = (self.x + self.padding, self.y + self.padding - 8)
        screen.blit(display_text, text_pos)
        self.draw_box(screen)

    def get_text(self):
        if self.text == self.default:
            return ''
        else:
            return self.text

    def input_text(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.active:
                self.active = self.rect.collidepoint(pygame.mouse.get_pos())
                self.text = ''

        elif self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
                self.filled = True
                self.text = self.text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text = self.text + event.unicode
