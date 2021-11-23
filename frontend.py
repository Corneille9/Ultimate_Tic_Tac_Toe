import pygame


def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def draw_big_pieces(Win, main_board, Square, Circle, Cross):
    for x in range(len(main_board)):
        for y in range(len(main_board)):
            if main_board[y][x] == -1:
                Win.blit(Circle, (x * Square, y * Square))

            if main_board[y][x] == 1:
                Win.blit(Cross, (x * Square, y * Square))


def draw_pieces(Win, Small_Circle, Small_Cross, Small_Square, board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == -1:
                Win.blit(Small_Circle, (x * Small_Square, y * Small_Square))

            if board[y][x] == 1:
                Win.blit(Small_Cross, (x * Small_Square, y * Small_Square))


def draw_board(Win, Line_color, Line_color_2, Width, Square, Small_Square, margin):
    Height = Width

    for move in range(0,3):
        for ab in range(0,3):
            for x in range(1,3):
                pygame.draw.line(Win,Line_color_2, (margin + Square*move, (x*Small_Square)+ab*Square), ((Square-margin)+Square*move,(x*Small_Square)+ab*Square),1)

            for bc in range(0,2):
                for y in range(3):
                    pygame.draw.line(Win, Line_color_2, (Small_Square + bc*Small_Square+move*Square, margin+ab*Square), (Small_Square + bc*Small_Square + move*Square, (Square-margin) + ab*Square),1)

    for i in range(1,3):
        pygame.draw.line(Win, Line_color, (0,Square*i),(Width, Square*i),2)
        pygame.draw.line(Win, Line_color, (Square*i,0),(Square*i, Height),2)
