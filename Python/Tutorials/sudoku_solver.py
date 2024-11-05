

def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for r in board:
        if r[col] == num:
            return False

    row_box = (row // 3) * 3
    col_box = (col // 3) * 3
    for y in range(row_box, row_box+3):
        for x in range(col_box, col_box+3):
            if board[y][x] == num:
                return False

    return True


def next_space(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return y, x

    return None, None


def solve(board):
    row, col = next_space(board)
    if row is None:
        return board

    for n in range(1, 10):
        if is_valid(board, row, col, n):
            board[row][col] = n
            if solve(board):
                return board
            board[row][col] = 0


def print_board(board):
    for n in board:
        print(n)


if __name__ == "__main__":
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    board = solve(board)
    print_board(board)
