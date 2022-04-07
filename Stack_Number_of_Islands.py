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
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# print(len(grid[0]))
print(numIslands_stack(grid))