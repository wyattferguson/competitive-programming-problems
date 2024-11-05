'''
Find the number of paths through the maze from the top left to bottom right
You can only travel down and to the right

Test Case:
    maze = [[1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1]]
'''


def print_maze(maze):
    for r in maze:
        print(r)
    print("")


if __name__ == "__main__":
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
    ]

    H = len(maze)
    W = len(maze[0])

    for col in range(H, 0, -1):
        for row in range(W, 0, -1):
            n = 1 if col == H and row == W else 0
            cur_x = row - 1
            cur_y = col - 1
            if maze[cur_y][cur_x] > 0:
                if col < H:
                    n += maze[col][cur_x]
                if row < W:
                    n += maze[cur_y][row]
                maze[cur_y][cur_x] = n

    print_maze(maze)
    print("Total Paths:", maze[0][0])
