# Importing Files
import pygame
import sys
import numpy as np
from Search import *
import classes as cls
import data_funcs as df

# Initializing PyGame
pygame.init()

# Setting Up Display
COL_COUNT = 7
ROW_COUNT = 6
SQUARE_SIZE = 100
screen_width = (COL_COUNT + 2) * SQUARE_SIZE
screen_height = (ROW_COUNT + 1) * SQUARE_SIZE + 10

# IMP Game Variables
fps = 60
clock = pygame.time.Clock()
pygame.display.set_caption("Connect 4")

title_icon = pygame.image.load("./title_icon.png")
pygame.display.set_icon(title_icon)

bg = (48, 61, 74, 21)  # (R, G, B)

CIRCLE_RADIUS = SQUARE_SIZE / 2 - 5

col_status = ''

FONT = pygame.font.SysFont("Segoe UI", 50)

# IMP Game Logic Variables
turn = 0
game_end = False
user_1 = ''
user_2 = ''
board = []
gameover_text_1, gameover_text_2 = '', ''
draw_text = FONT.render("Its a DRAW!", True, (200, 200, 200, 200))


# ------------------------- Game Graphic Functions -------------------------


# Creates Screen
def set_screen():
    return pygame.display.set_mode((screen_width, screen_height))


screen = set_screen()


# Draws Game Board on Screen
def draw_board(red_coin, yellow_coin):
    pygame.draw.rect(screen, (39, 68, 137, 46),
                     (SQUARE_SIZE, SQUARE_SIZE, COL_COUNT * SQUARE_SIZE + 5, ROW_COUNT * SQUARE_SIZE),
                     border_radius=10)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # Draw Empty Spaces
            if board[r][c] == 0:
                pygame.draw.circle(screen, (0, 0, 0),
                                   ((c + 1) * SQUARE_SIZE + SQUARE_SIZE / 2 + 2,
                                    (r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2),
                                   CIRCLE_RADIUS)
            # Draw Red Coins
            elif board[r][c] == 1:
                red_coin.draw_coin(screen, ((c + 1) * SQUARE_SIZE + SQUARE_SIZE / 2 + 2,
                                            (r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2),
                                   CIRCLE_RADIUS)
            # Draw Yellow Coins
            elif board[r][c] == 2:
                yellow_coin.draw_coin(screen,
                                      ((c + 1) * SQUARE_SIZE + SQUARE_SIZE / 2 + 2,
                                       (r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2),
                                      CIRCLE_RADIUS)

            pygame.draw.line(screen, (39, 68, 137, 46), ((c + 1) * SQUARE_SIZE + 2, 0),
                             ((c + 1) * SQUARE_SIZE + 2, SQUARE_SIZE + 5), width=6)
    pygame.draw.line(screen, (39, 68, 137, 46), (8 * SQUARE_SIZE + 1, 0),
                     (8 * SQUARE_SIZE + 1, SQUARE_SIZE + 5),
                     width=7)


# Draws Player-Colour Indicator
def draw_player_colour(red_coin, yellow_coin):
    Font = pygame.font.SysFont("Comic Sans MS", 20, bold=True)
    red_text = Font.render(f"{user_1}", True, (255, 10, 10))
    # Red Coin
    pygame.draw.rect(screen, (39, 68, 137, 46), (SQUARE_SIZE // 2 - CIRCLE_RADIUS + 12,
                                                 (COL_COUNT * SQUARE_SIZE) / 2 - CIRCLE_RADIUS + 17,
                                                 CIRCLE_RADIUS + 15, CIRCLE_RADIUS + 15),
                     border_radius=10)

    red_coin.draw_coin(screen, (SQUARE_SIZE // 2 - 2, (COL_COUNT * SQUARE_SIZE) // 2 + 2), CIRCLE_RADIUS - 20)
    screen.blit(red_text,
                (SQUARE_SIZE // 2 - CIRCLE_RADIUS + 12 + (CIRCLE_RADIUS + 15) // 2 - red_text.get_width() // 2,
                 (COL_COUNT * SQUARE_SIZE) / 2 + 30))

    # Yellow Coin
    yellow_text = Font.render(f"{user_2}", True, (255, 255, 10))
    pygame.draw.rect(screen, (39, 68, 137, 46), (screen_width - SQUARE_SIZE // 2 + 5 - CIRCLE_RADIUS + 12,
                                                 (COL_COUNT * SQUARE_SIZE) // 2 - CIRCLE_RADIUS + 17,
                                                 CIRCLE_RADIUS + 15, CIRCLE_RADIUS + 15),
                     border_radius=10)

    yellow_coin.draw_coin(screen, (screen_width - SQUARE_SIZE // 2 + 2.75, (COL_COUNT * SQUARE_SIZE) // 2 + 2),
                          CIRCLE_RADIUS - 20)

    screen.blit(yellow_text,
                (screen_width - SQUARE_SIZE // 2 + 5 - CIRCLE_RADIUS + 12 + (
                        CIRCLE_RADIUS + 15) // 2 - yellow_text.get_width() // 2,
                 (COL_COUNT * SQUARE_SIZE) // 2 + 30))


# Executes the game over screen. [Runs When a Player Wins]
def game_over(piece, is_draw=False):
    global game_end, board, red_coin, yellow_coin
    if is_draw:
        draw_board(red_coin, yellow_coin)
    pygame.display.update()
    pygame.time.delay(1200)
    if not is_draw:
        if piece == 1:
            game_over_text = gameover_text_1
            df.update_player_details(user_1, user_2)

        else:
            game_over_text = gameover_text_2
            df.update_player_details(user_2, user_1)
    else:
        game_over_text = draw_text
        df.update_player_details(user_1, user_2, True)

    screen.fill((0, 0, 0))
    screen.blit(game_over_text, (
        screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(1500)

    del red_coin
    del yellow_coin
    game_end = True
    return


# ------------------------ Game Logic Functions ------------------------

# Creates a 2d list, grid
def create_board():
    return np.zeros((6, 7))


# Checks If the location to drop piece in IS FREE/ EXISTS
def is_valid_location(col):
    return board[0][col - 1] == 0


# Gets The Top-most free spot In a COLUMN
def get_next_row(col):
    for row in range(ROW_COUNT - 1, -1, -1):
        if board[row][col - 1] == 0:
            return row


# Drops the piece in the grid
def drop_piece(row, col, piece):
    global board
    board[row][col - 1] = piece
    search(row, col - 1, piece)


# Uses function in Search file to check for WIN
def search(row, col, piece):
    if search_right_or_left(board, row, col, piece) or search_up_or_down(board, row, col, piece):
        draw_board(red_coin, yellow_coin)
        game_over(piece)
    elif search_right_diagonal(board, row, col, piece) or search_left_diagonal(board, row, col, piece):
        draw_board(red_coin, yellow_coin)
        game_over(piece)
    else:
        if all(value == 6 for value in col_status.values()):
            game_over(piece, is_draw=True)


# Function to control game events like press of mouse button, etc.
def event_controller(red_coin, yellow_coin):
    global turn

    # Catching events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            red_coin.posx = event.pos[0]
            yellow_coin.posx = event.pos[0]

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            if not 0 <= posx <= SQUARE_SIZE:
                if turn == 0:
                    col = int(red_coin.posx // SQUARE_SIZE)
                    if is_valid_location(col):
                        r = get_next_row(col)
                        if col_status[col] != 6:
                            col_status[col] += 1
                            drop_piece(r, col, 1)
                            turn += 1

                elif turn == 1:
                    col = int(yellow_coin.posx // SQUARE_SIZE)
                    if is_valid_location(col):
                        r = get_next_row(col)
                        if col_status[col] != 6:
                            col_status[col] += 1
                            drop_piece(r, col, 2)
                            turn += 1

                turn %= 2


# ------------------------ Different Screens & Related Functions ------------------------
def player_login_screen():
    run = True

    red_box = cls.TextBox(275, 200, 40, 30, 500, (210, 0, 0), (129, 251, 240), (0, 210, 0), 5,
                          "Enter Username for Player Red")
    yellow_box = cls.TextBox(275, 300, 40, 30, 500, (210, 0, 0), (129, 251, 240), (0, 210, 0), 5,
                             "Enter Username for Player Yellow")
    start_button = cls.Button(375, 450, 30, 30, (210, 0, 0), (0, 210, 0), start_game, text="Start Game")

    while run:

        mouse_posX, mouse_posY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            red_box.input_text(event)
            yellow_box.input_text(event)
            red_text = red_box.get_text()
            yellow_text = yellow_box.get_text()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collided(mouse_posX, mouse_posY):
                    start_button.click(param=(red_text, yellow_text))
                    run = False

        screen.fill(bg)

        pygame.draw.rect(screen, (39, 68, 137, 46), (165, 200, 70, 70),
                         border_radius=10)

        pygame.draw.circle(screen, (210, 0, 0), (200, 235), 30)

        pygame.draw.rect(screen, (39, 68, 137, 46), (165, 300, 70, 70),
                         border_radius=10)

        pygame.draw.circle(screen, (255, 255, 10), (200, 335), 30)

        red_box.render_text(screen)
        yellow_box.render_text(screen)
        red_box.draw_box(screen)
        yellow_box.draw_box(screen)
        start_button.draw_button(screen, mouse_posX, mouse_posY)
        clock.tick(fps)
        pygame.display.update()


def start_game(users):
    df.make_player(users)
    gameloop()


def gameloop():
    global user_1, user_2, board, turn, red_coin, yellow_coin, col_status
    global gameover_text_1, gameover_text_2, game_end

    board = create_board()
    game_end = False

    turn = 0
    red_coin = cls.Coin(SQUARE_SIZE + CIRCLE_RADIUS // 2, screen_width - SQUARE_SIZE - CIRCLE_RADIUS // 2, SQUARE_SIZE,
                        CIRCLE_RADIUS, (255, 10, 10))
    yellow_coin = cls.Coin(SQUARE_SIZE + CIRCLE_RADIUS // 2, screen_width - SQUARE_SIZE - CIRCLE_RADIUS // 2,
                           SQUARE_SIZE,
                           CIRCLE_RADIUS, (255, 255, 10))

    col_status = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    user_1, user_2 = df.get_players()
    gameover_text_1 = FONT.render(f"{user_1} Wins!", True, (200, 200, 200, 200))
    gameover_text_2 = FONT.render(f"{user_2} Wins!", True, (200, 200, 200, 200))

    while not game_end:
        try:
            pygame.display.update()
            event_controller(red_coin, yellow_coin)
            if game_end:
                break
            screen.fill(bg)
            draw_board(red_coin, yellow_coin)
            draw_player_colour(red_coin, yellow_coin)
            if turn == 0:
                red_coin.draw_cursor(screen, SQUARE_SIZE)
            elif turn == 1:
                yellow_coin.draw_cursor(screen, SQUARE_SIZE)

            clock.tick(fps)
            pygame.display.update()
        except pygame.error:
            pass


def display_details(user):
    data = df.get_user_details(user)
    if type(data) != str:
        wins = data[1]
        loses = data[2]
        draws = data[3]

        win_text = FONT.render("Games Won: " + str(wins), True, (255, 255, 255))
        lost_text = FONT.render("Games Lost: " + str(loses), True, (255, 255, 255))
        draw_details = FONT.render("Games Drawn: " + str(draws), True, (255, 255, 255))

        return win_text, lost_text, draw_details
    else:
        return data, FONT.render(data, True, (255, 255, 255))


def details_screen():
    running = True

    get_details_button = cls.Button(380, 250, 30, 30, (210, 0, 0), (0, 210, 0), display_details,
                                    text="Get Details")
    return_button = cls.Button(30, 30, 30, 30, (210, 0, 0), (0, 210, 0), main_menu, text="Back")

    text_box = cls.TextBox(200, 150, 40, 30, 500, (210, 0, 0), (129, 251, 240), (0, 210, 0), 5, "Enter Username")

    while running:

        mouse_posX, mouse_posY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            text = text_box.get_text()
            text_box.input_text(event)

            if event.type == pygame.MOUSEBUTTONUP:
                if return_button.collided(mouse_posX, mouse_posY):
                    return_button.click()
                    running = False

                if get_details_button.collided(mouse_posX, mouse_posY):
                    details = get_details_button.click(param=text)
        screen.fill(bg)
        text_box.render_text(screen)
        try:
            if type(details[0]) != str:
                screen.blit(details[0], (100, 400))
                screen.blit(details[1], (520, 400))
                screen.blit(details[2], (275, 500))
            else:
                screen.blit(details[1], (250, 400))
        except UnboundLocalError:
            pass
        get_details_button.draw_button(screen, mouse_posX, mouse_posY)
        return_button.draw_button(screen, mouse_posX, mouse_posY)
        clock.tick(fps)
        pygame.display.update()


def main_menu():
    running = True

    title_img = pygame.image.load('./game_logo.png')
    title_img = pygame.transform.scale(title_img, (700, 243))

    play_button = cls.Button(260, 500, 30, 30, (210, 0, 0), (0, 210, 0), player_login_screen, "Play")
    view_details_button = cls.Button(360, 500, 30, 30, (210, 0, 0), (0, 210, 0), details_screen, "View Details")
    quit_button = cls.Button(538, 500, 30, 30, (210, 0, 0), (0, 210, 0), sys.exit, "Quit")

    while running:

        mouse_posX, mouse_posY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collided(mouse_posX, mouse_posY):
                    play_button.click()

                if view_details_button.collided(mouse_posX, mouse_posY):
                    view_details_button.click()

                if quit_button.collided(mouse_posX, mouse_posY):
                    running = False
                    pygame.quit()
                    quit_button.click()

        screen.fill(bg)
        screen.blit(title_img, ((screen_width // 2) - (title_img.get_width() // 2),
                                (screen_height // 2) - (title_img.get_height())))

        play_button.draw_button(screen, mouse_posX, mouse_posY)
        view_details_button.draw_button(screen, mouse_posX, mouse_posY)
        quit_button.draw_button(screen, mouse_posX, mouse_posY)

        clock.tick(fps)
        pygame.display.update()


if __name__ == '__main__':
    main_menu()
