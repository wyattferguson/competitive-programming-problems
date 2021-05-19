
def is_valid(board, row, col):
    if row >= 0 and col >= 0 and row < 8 and col < 8:
        if board[row][col] == 0:
            return True
    return False


def solve(board, row=0, col=0, cnt=2):
    moves = [[2, 1], [1, 2], [-2, -1], [-2, 1], [2, -1],
             [-1, -2], [1, -2], [-1, 2]]

    if cnt >= 64:
        return True

    for m in moves:
        next_row = row + m[0]
        next_col = col + m[1]

        if is_valid(board, next_row, next_col):
            board[next_row][next_col] = cnt
            if solve(board, next_row, next_col, cnt+1):
                return True
            board[next_row][next_col] = 0
    return False


def print_board(board):
    for n in board:
        print(n)


if __name__ == "__main__":
    board = [[0] * 8 for _ in range(8)]
    board[0][0] = 1  # knights start
    solve(board)
    print_board(board)
