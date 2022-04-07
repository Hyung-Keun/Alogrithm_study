# def validPath(n, edges, source, destination):
#     dic = [set() for _ in range(n)]
#     for edge in edges:
#         dic[edge[0]].add(edge[1])
#         dic[edge[1]].add(edge[0])
#         # print(edge[0])
#
#         print(edge[1])
#
#     visit = [0] * n
#     visit[source] = 0 #우선 초기화시켜놓는다. 방문했는지 안했는지를 확인할용도.
#     path = [source] #경로탐색저장
#     while path: #경로에 우선 무엇인가있다. 0. 그러면 일한다.
#         popElement = path.pop()
#         if popElement == destination:
#             return True
#
#         for element in dic[popElement]:
#             if visit[element] == 0:
#                 visit[element] = 1
#                 path.append(element)
#     return False
# #

graph = [[1, 2], [3], [3], []]
print(len(graph))

def validPath(n, edges, start, end):

    adjacency_list = [[] for _ in range(n)]
    for a, b in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    stack = [start]
    seen = set()

    while stack:
        # Get the current node.
        node = stack.pop()

        # Check if we have reached the target node.
        if node == end:
            return True

        # Check if we've already visited this node.
        if node in seen:
            continue
        seen.add(node)

        # Add all neighbors to the stack.
        for neighbor in adjacency_list[node]:
            stack.append(neighbor)

    return False
print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2 ))