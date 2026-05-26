import pygame
import sys

pygame.init()

WIDTH = 640
HEIGHT = 640
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS

LIGHT_COLOR = (240, 217, 181)
DARK_COLOR = (181, 136, 99)
TEXT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess Game")

font = pygame.font.SysFont("Arial", 40)

board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

selected_piece = None
current_turn = "white"


def draw_board():
    for row in range(ROWS):
        for col in range(COLS):

            if (row + col) % 2 == 0:
                color = LIGHT_COLOR
            else:
                color = DARK_COLOR

            pygame.draw.rect(
                screen,
                color,
                (
                    col * SQUARE_SIZE,
                    row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE
                )
            )


def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):

            piece = board[row][col]

            if piece != "":
                piece_text = font.render(piece, True, TEXT_COLOR)

                screen.blit(
                    piece_text,
                    (
                        col * SQUARE_SIZE + 20,
                        row * SQUARE_SIZE + 15
                    )
                )


def move_piece(start_pos, end_pos):

    global current_turn

    start_row, start_col = start_pos
    end_row, end_col = end_pos

    piece = board[start_row][start_col]

    if piece == "":
        return

    if current_turn == "white" and piece.islower():
        return

    if current_turn == "black" and piece.isupper():
        return

    board[end_row][end_col] = piece
    board[start_row][start_col] = ""

    if current_turn == "white":
        current_turn = "black"
    else:
        current_turn = "white"


running = True

while running:

    draw_board()
    draw_pieces()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE

            if selected_piece is None:
                selected_piece = (clicked_row, clicked_col)

            else:
                move_piece(
                    selected_piece,
                    (clicked_row, clicked_col)
                )

                selected_piece = None

    pygame.display.update()
