

def is_valid(board, row, col):
    # check row
    if 1 in board[row]:
        return False

    # check col
    for r in board:
        if r[col] == 1:
            return False

    # check diagonal
    for i in range(1, 8):
        if row + i < 8:
            if col + i < 8 and board[row + i][col+i] == 1:
                return False

            if col - i >= 0 and board[row + i][col-i] == 1:
                return False

        if row - i >= 0:
            if col - i >= 0 and board[row - i][col-i] == 1:
                return False
            if col + i < 8 and board[row - i][col+i] == 1:
                return False
    return True


def solve(board, row=0, col=0):
    if col >= 8:
        return True

    for r in range(0, 8):
        if is_valid(board, r, col):
            board[r][col] = 1
            if solve(board, r, col + 1):
                return board
            board[r][col] = 0


def print_board(board):
    for y in board:
        print(y)


if __name__ == "__main__":
    board = [[0] * 8 for _ in range(8)]
    solved = solve(board)
    print_board(solved)
