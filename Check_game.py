def valid_locations(board, main_board, x, y, box):
    if box is None or [x, y] in box:
        if board[y][x] == 0 and main_board[y // 3][x // 3] == 0:
            return True
    return False


def set_locations(board, main_board, x, y, player, box):
    if valid_locations(board, main_board, x, y, box):
        board[y][x] = player
        return True
    return False


def place_big_board(main_board, x, y, player):
    main_board[y][x] = player


def get_next_box(x, y):
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3):
                    for h in range(3):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(0, 7, 3):
        for j in range(1, 8, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3):
                    for h in range(3, 6):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(0, 7, 3):
        for j in range(2, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3):
                    for h in range(6, 9):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(1, 8, 3):
        for j in range(0, 7, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3, 6):
                    for h in range(3):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3, 6):
                    for h in range(3, 6):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(1, 8, 3):
        for j in range(2, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(3, 6):
                    for h in range(6, 9):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(2, 9, 3):
        for j in range(0, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(6, 9):
                    for h in range(3):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(2, 9, 3):
        for j in range(1, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []
                for k in range(6, 9):
                    for h in range(3, 6):
                        possible_moves.append([k, h])
                return possible_moves

    for i in range(2, 9, 3):
        for j in range(2, 9, 3):
            if (x, y) == (i, j):
                possible_moves = []

                for k in range(6, 9):
                    for h in range(6, 9):
                        possible_moves.append([k, h])
                return possible_moves


def is_empty_box(board, box, x, y):
    empty_cells = []
    for index, values in enumerate(box):
        if board[values[1]][values[0]] == 0:
            empty_cells.append(values)
    if len(empty_cells) == 0:
        return False
    else:
        return True


def get_possible_moves(board, x, y):
    box = get_next_box(x, y)
    return box


def validate_box(board, main_board, box, x, y):
    if is_empty_box(board, box, x, y) and main_board[box[0][1] // 3][box[0][1] // 3] == 0:
        return box
    else:
        return empty_cells_small_boards(board)


def empty_cells_small_boards(board):
    empty_cells = []

    for y, row in enumerate(board):
        for x, case in enumerate(row):
            if case == 0:
                empty_cells.append([x, y])

    return empty_cells


def empty_cells_big_board(main_board):
    empty_cells = []

    for y, row in enumerate(main_board):
        for x, case in enumerate(row):
            if case == 0:
                empty_cells.append([x, y])

    return empty_cells


def check_empty_cells(board):
    if len(empty_cells_small_boards(board)) == 0:
        print("personne ne gagne")


def check_big_board(main_board, player):
    for row in main_board:
        row_stock = []
        for i in range(len(row)):
            row_stock.append(row[i])
        if row_stock.count(player) == len(row_stock):
            print(player, "win")
            return True

    for col in range(len(main_board)):
        col_stock = []
        for row in main_board:
            col_stock.append(row[col])
        if col_stock.count(player) == len(col_stock):
            print(player, "win")
            return True

    diag_1 = []
    for index in range(len(main_board)):
        diag_1.append(main_board[index][index])
    if diag_1.count(player) == len(diag_1):
        print(player, "win")
        return True

    diag_2 = []
    for index, rev_index in enumerate(reversed(range(len(main_board)))):
        diag_2.append(main_board[index][rev_index])
    if diag_2.count(player) == len(diag_2):
        print(player, "win")
        return True

    if len(empty_cells_big_board(main_board)) == 0:
        print("No One Win")
        return True


def check_horizontally(board, main_board, player):
    good = False
    for i in range(0, 7, 3):
        for index, row in enumerate(board):
            if row[i] == row[i + 1] == row[i + 2] == player:
                print(player, " fait un alignement horizontal")
                good = True
            if good:
                place_big_board(main_board, i // 3, index // 3, player)
                good = False


def check_vertically(board, main_board, player):
    good_col = False
    for index in range(len(board)):
        check = []
        for i, row in enumerate(board):
            check.append(row[index])

            if len(check) >= 3:
                if len(check) == check.count(player):
                    print(player, " fait un alignement vertical")
                    good_col = True

                    if good_col:
                        place_big_board(main_board, index // 3, i // 3, player)
                        good_col = False
                        check.clear()
                check.clear()


def check_diagonals(board, main_board, player):
    for x in range(0, 8, 3):
        stock_index = []
        for y in range(0, 8, 3):
            stock_index.append(board[y][x])
            for i in range(1, 3):
                stock_index.append(board[y + i][x + i])

                if len(stock_index) >= 3:
                    if stock_index.count(player) == len(stock_index):
                        a, b = y + i, x + i
                        print(player, " fait un alignement dans une diagonale")
                        place_big_board(main_board, b // 3, a // 3, player)
                        stock_index.clear()
                else:
                    stock_index.clear()

    for x in range(0, 9, 3):
        stock_nindex = []
        for y in range(2, 9, 3):
            for i in range(3):
                stock_nindex.append(board[y - i][x + i])

                if len(stock_nindex) >= 3:
                    if stock_nindex.count(player) == len(stock_nindex):
                        a, b = y - 1, x + i
                        print(player, " fait un alignement dans une diagonale")
                        place_big_board(main_board, b // 3, a // 3, player)
                        stock_nindex.clear()
                else:
                    stock_nindex.clear()


def check_game(board, main_board, player):
    check_horizontally(board, main_board, player)
    check_vertically(board, main_board, player)
    check_diagonals(board, main_board, player)
    check_empty_cells(board)
