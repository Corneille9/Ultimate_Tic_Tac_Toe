import pygame
import os
import random

from Check_game import set_locations, check_game, get_possible_moves, validate_box, check_big_board
from board import New_Board
from frontend import draw_big_pieces, draw_pieces, draw_board, fill

pygame.font.init()

Width, Height = 510, 510
Square = Width // 3
Small_Square = Square // 3

margin = Width // 3

Win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ultimate Tic Tac Toe")
Clock = pygame.time.Clock()

Small_Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Small_Square, Small_Square))
Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cross.png")), (Square, Square))

Small_Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Small_Square, Small_Square))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cross.png")), (Square, Square))

Bg = (0, 0, 0)
Line_color = (211, 211, 211)
Line_color_2 = (250, 0, 0)

Board = New_Board()


def update_window(Win, main_board, small_board):
    Win.fill(Bg)
    draw_pieces(Win, Small_Circle, Small_Cross, Small_Square, small_board)
    draw_board(Win, Line_color, Line_color_2, Width, Square, Small_Square, margin)
    draw_big_pieces(Win, main_board, Square, Circle, Cross)
    pygame.display.update()


def main():
    run = True
    game_over = False
    green = (0, 178, 0, 0)

    FPS = 60

    box = None

    Player_1 = 1
    Player_2 = -1

    main_board = Board.create_board()
    small_board = Board.every_small_board()

    fill(Circle, green)
    fill(Small_Circle, green)

    turn = random.choice([1, -1])

    while run:
        Clock.tick(FPS)

        update_window(Win, main_board, small_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    if set_locations(small_board, main_board, pos[0]//Small_Square, pos[1]//Small_Square, turn, box):
                        check_game(small_board, main_board, turn)
                        new_box = get_possible_moves(small_board, pos[0]//Small_Square, pos[1]//Small_Square)

                        box = validate_box(small_board, main_board, new_box, pos[0]//Small_Square, pos[1]//Small_Square)

                        if check_big_board(main_board, turn):
                            game_over = True

                        if turn == Player_1:
                            turn = Player_2
                        else:
                            turn = Player_1



main()
