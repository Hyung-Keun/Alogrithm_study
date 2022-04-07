#stack으로 풀기
def island_dfs_stack(grid): #그리드가 들어왔을때
    #탐색범위를 한정, 상대적인 x좌표와 y좌표
    dx = [0, 0, 1, -1] #행 (가로) 좌우
    dy = [1, -1, 0, 0] #열 (세로) 상하
    rows, cols = len(grid), len(grid[0]) #여기다가 저장하고
    cnt = 0

    for row in range(rows): #이중 for문 돈다.
        for col in range(cols):
            if grid[row][col] != '1':#내가 방문한곳이 1인지 아닌지 확인한다. 1인곳만 방문한다
                continue

            cnt += 1 #섬의 숫자를 올린다.
            stack = [(row, col)] #점의 좌표를 스택에 넣는다.

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 3
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# print(len(grid[0]))
print(island_dfs_stack(grid))