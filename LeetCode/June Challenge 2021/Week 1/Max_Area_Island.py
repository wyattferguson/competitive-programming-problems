'''
Name:Max Area of Island
URL: https://bit.ly/3yRkOiR
Date: June 1, 2021

Test Cases:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[
    0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        def dive(grid, row, col):
            cur_cnt = 1
            moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for y, x in moves:
                y_move = col+y
                x_move = row+x
                if y_move >= 0 and x_move >= 0 and y_move < M and x_move < N and grid[y_move][x_move] == 1:
                    grid[y_move][x_move] = 2
                    cur_cnt += dive(grid, x_move, y_move)

            return cur_cnt

        island = 0
        M, N = len(grid), len(grid[0])
        for x in range(N):
            for y in range(M):
                if grid[y][x] == 1:
                    grid[y][x] = 2
                    island = max(island, dive(grid, x, y))

        return island


if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    solve = Solution()
    print(solve.maxAreaOfIsland(grid))
