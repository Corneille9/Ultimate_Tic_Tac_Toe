class New_Board:
    def __init__(self):
        self.test = "test"

    def create_board(self):
        return [[0 for x in range(3)] for y in range(3)]

    def every_small_board(self):
        return [[0 for y in range(9)] for y in range(9)]

    def reset(self, board, main_board, game_over):
        if game_over:
            for x, row in enumerate(board):
                for y in range(len(row)):
                    board[y][x] = 0

            for x, row in enumerate(main_board):
                for y in range(len(row)):
                    main_board[y][x] = 0
