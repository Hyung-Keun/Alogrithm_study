import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

directions = [0, 1, 0, -1, 0]

for tc in range(int(input())):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + directions[i]
            ny = y + directions[i + 1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print("Problem {}: {}".format(tc+1, distance[n - 1][n - 1]))


