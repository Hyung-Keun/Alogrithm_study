def numIslands_rec(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
        grid[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

print(numIslands_rec())
#stack
def numIslands_stack(grid):
    islands = 0  # number of islands
    stack = []  # stack for DFS
    m = len(grid)  # number of rows
    n = len(grid[0])  # number of columns

    # start checking all elements in grid
    for i in range(m):
        for j in range(n):
            if (grid[i][j] == "1"):
                islands += 1  # found 1, start a new island
                grid[i][j] = "x"  # mark visited by "x"
            else:
                continue  # ignore if 0 or x

            stack.append((i, j))
            # perform DFS on stack
            while (len(stack)):

                temp_i, temp_j = stack.pop()
                grid[temp_i][temp_j] = "x"  # mark as visited

                if (temp_i + 1 < m):  # check for validity of index
                    if (grid[temp_i + 1][temp_j] == "1"):  # if 1, add to stack
                        stack.append((temp_i + 1, temp_j))
                if (temp_i - 1 >= 0):
                    if (grid[temp_i - 1][temp_j] == "1"):
                        stack.append((temp_i - 1, temp_j))
                if (temp_j + 1 < n):
                    if (grid[temp_i][temp_j + 1] == "1"):
                        stack.append((temp_i, temp_j + 1))
                if (temp_j - 1 >= 0):
                    if (grid[temp_i][temp_j - 1] == "1"):
                        stack.append((temp_i, temp_j - 1))

    return islands

from collections import deque
def numIslands_q(grid) -> int:
    directions = [0, 1, 0, -1, 0]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '1':
                continue

            count += 1
            q = deque([(r, c)])

            while q:
                a, b = q.popleft()

                for k in range(4):
                    nx = a + directions[k]
                    ny = b + directions[k + 1]

                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue

                    grid[nx][ny] = '0'
                    q.append((nx, ny))

    return count
