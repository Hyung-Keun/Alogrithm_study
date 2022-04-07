from collections import deque
import sys
#입력하자 인풋 확인하고, 문제 잘 읽어서 형식대로 절차 진행하자
#백준문제풀때 눈감고 import sys 써주고
input = sys. stdin.readline # 이것도 써주고
rows, cols = map(int, input().split()) #이것도 써주는데, map부터가 중요

matrix = [] #행렬 인풋 받아올준비합시다.

for _ in range(rows):#인풋받은 숫자들을 바탕으로 행렬을 만들어줍시다.
    matrix.append(list(map(int, input().strip()))) #정수로 받아오게 해준다.

visited = [[[0] * 2 for _ in range(cols)] for _ in range(rows)] #모든 구역을 0으로 깔아준다 -> 방문 안했다는뜻으로
visited[0][0][0] = 1 #3차원 배열로 벽을 부수는게 가능한지 불가능한지 입력해준다. visited[0][0][0]: 벽안부수고감 visited[0][0][1]:벽부수고감
directions = [0, 1, 0, -1, 0] #네비게이션기능이라고 내가 부른다. 위 아래 왼쪽 오른쪽 조건을 검사해서 이동

def bfs(x, y, z):
    q = deque() #bfs최단경로탐색을 위해서는 큐를 사용 해야하고, 그렇기때문에 데크를 사용한다.
    q.append((x, y, z)) #받아온 x, y, z로 시작! 여기선 0,0,0 에서 시작
    while q:
        a, b, c = q.popleft() # 맨처음에 들어간것부터 들어간다 (0, 0, 0) 시작
        if a == rows - 1 and b == cols - 1: #인풋값 좌표가 입력한 행렬의 끝좌표이면 / 도달한 경우
            return visited[a][b][c] #visited[5][3][c] 바로리턴해버려
        for k in range(4): #위 아래 왼쪽 오른쪽 검사실시!
            nx = a + directions[k] #위에 제시한 directions대로 x 한칸 옆에가서 검사하고
            ny = b + directions[k+1] #y한칸 가서 검사하기
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue # 내가 입력한 행렬위에서 네비게이션이 움직이지 않으면 위로올라가.
            if matrix[nx][ny] == 1 and c == 0: # 벽이 있고 + 벽 아직 안부순상태
                visited[nx][ny][1] = visited[a][b][0] + 1 #이전상태 (벽 안부순상태) 에다가 부수고 갔다는 것을 말해준다
                q.append((nx, ny, 1)) #큐에다가 저장 #벽 부수고 간걸로 저장
            elif matrix[nx][ny] == 0 and visited[nx][ny][c] == 0: #네비했는데, 벽없고,  방문한적없을때
                visited[nx][ny][c] = visited[a][b][c] + 1 #한칸 이동시키고
                q.append((nx, ny, c)) #큐에다가 저장
    return -1 #목표지점 도달 못하면 -1 리턴

print(bfs(0, 0, 0))





