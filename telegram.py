import sys
import heapq
'''
3 2 1
1 2 4
1 3 2
'''
input = sys.stdin.readline
INF = int(1e9)

N, M, start = map(int, input().split()) #도시의 개수, 통로의 개수, 메세지보내는 곳
graph = [[] for i in range(N + 1)]
# print(graph)
distance = [INF] * (N + 1)
# print(distance)

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

count = 0

max_distance = 0
for d in distance:
    if d!= INF:
        count += 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)