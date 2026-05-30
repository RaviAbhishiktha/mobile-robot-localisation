# CO2: Mobile Robot Localization using BFS

from collections import deque

GRID = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

ROWS = len(GRID)
COLS = len(GRID[0])

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy

            if (0 <= nx < ROWS and
                0 <= ny < COLS and
                GRID[nx][ny] == 0):
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

start = (0, 0)
goal = (3, 3)

path = bfs(start, goal)

print("Shortest Path:")
print(path)
