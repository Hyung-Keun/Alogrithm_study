import sys

input = sys.stdin.readline

V, E = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[INF] * (V + 1) for _ in range(V + 1)]
# print(graph)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
# print(graph)

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
for i in range(1, V + 1):
    answer = min(answer, graph[i][i]) #사이클이니까 i로한다
if answer == INF:
    print(-1)
else:
    print(answer)