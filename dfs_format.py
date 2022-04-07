#입력받아오기
#dfs양식
import sys
input = sys.stdin.readline
I = int(input())
#입력
matrix = []
for _ in range(I):
    row = list(input().rstrip())
    matrix.append(row)
print(matrix)
visited = [[0 for a in range(I)] for b in range(I)] #0인 리스트 만들어주기
# print(visited)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]