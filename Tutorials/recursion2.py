"""
Count all paths from the top right of grid to bottom left. You can only move down and right. Your input is a NxM grid.

"""

# reverse the search start at bottom right
def path(x, y):
    if x == 1 or y == 1:
        return 1

    return path(x - 1, y) + path(x, y - 1)


n = 2
m = 3
cnt = path(n, m)
print(cnt)
