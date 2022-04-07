import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

input_smth = int(input())

matrix = []

for _ in range(input_smth):
    row = list(input().strip())
    matrix.append(row)
#print(matrix)
#-------------------------------------------------
#여기라인까지 백준 문제풀때, 여러개 값을 입력받아야 할때, 써야하는 것들. 외우면 좋다, 아니 외우자
visited = [[False for _ in range(input_smth)] for _ in range(input_smth)]
#false 로 채워놓는다. 방문을 안했다는 뜻이다. 방문을 했을경우에는 True로 바꿀 생각을한다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#좌, 우, 위, 아래를 조사해서, 좌표로 생각해서, 색깔 같으면 dfs재귀 돌린다.
#dfs 재귀로 풀 생각을 하면서 연습해봅시다.

def dfs(x, y):#지금 시작하는 좌표를 재귀할겁니다. 이걸로 매트릭스를 훑을겁니다.
    visited[x][y] = True #방문을 했으니까 True로 바꿔줍니다~
    for search in range(4): # 좌, 우, 위, 아래 검사를 시작~
        nx = x + dx[search] #방문한 좌표 x 한칸 옆에로 이동해서 검사 실시 준비.
        ny = y + dy[search] #방문한 좌표 y 한칸 옆에로 이동해서 검사 실시 준비.
        if nx >= 0 and nx < input_smth and ny >= 0 and ny < input_smth: #양옆 위아래 검사하는데 입력받은 행렬위 밖으로 나가지 않을경우에~
            if visited[nx][ny] == False and matrix[nx][ny] == matrix[x][y]: #만약에 현재좌표 색깔이랑 검사한 색깔이랑 맞으면 dfs에 넣어준다.
                dfs(nx, ny) #이게 무슨말이냐면, 검사하고 색깔 같으면, 옆으로 한칸 이동하면서, 새좌표로 다시 검사 시작.
#-------------------------------------------------
#게임기 같은 느낌으로 생각해주고 편하게 익숙하게 생각하자.

#일반모드
count1 = 0 #일반모드일경우의 영역 세주기
for i in range(input_smth):
    for j in range(input_smth):
        if visited[i][j] == False:
            dfs(i, j)
            count1 += 1

#적록색약이 있으면 R을 G로 바꿔준다. 그상태에서 카운트를 세서 영역 카운트.
for i in range(input_smth): #우선 좌표를 적록색모드로 다 바꿔준다.
    for j in range(input_smth):
        if matrix[i][j] == 'R': #빨간색이면 초록색으로 바꾸기
            matrix[i][j] = 'G'

visited = [[False for _ in range(input_smth)] for _ in range(input_smth)]
#방문하지 않은상태로 초기화를 해줘야한다. 그렇지않으면 일반모드 + 색약모드를 진행하기때문이다. 다시 모든것이 아무것도 방문안된상태로 해주고 시작한다.
count2 = 0 #적록색약모드일경우의 영역세주기
for i in range(input_smth):
    for j in range(input_smth):
        if visited[i][j] == False:
            dfs(i, j)
            count2 += 1

#-------------------------------------------------
#일반모드와 적색약모드 두개가 있다고 생각하자.

print(count1, count2) #마지막으로 일반모드 적색약모드 영역 몇개인지 카운트 출력! 한번 출력해볼까!

