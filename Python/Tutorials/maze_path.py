import time


def is_valid(maze, row, col):
    if row >= 0 and col >= 0 and row < 10 and col < 10:
        if maze[row][col] == 1 or maze[row][col] == 'X':
            return True
    return False


def solve(maze, row=0, col=0):
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if (row, col) == (9, 9):
        return maze

    for m in moves:
        next_row = row + m[0]
        next_col = col + m[1]

        if is_valid(maze, next_row, next_col):
            maze[next_row][next_col] = 2
            if solve(maze, next_row, next_col):
                return maze
            maze[next_row][next_col] = 1


def print_board(board):
    for n in board:
        print(n)


if __name__ == "__main__":
    start = time.time()
    # Start at (0,0) and get to X (9,9)
    maze = [
        [2, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 'X']
    ]

    maze = solve(maze)
    print_board(maze)
    print(f"time taken: {time.time() - start}")
