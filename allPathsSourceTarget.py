from collections import deque


def allPathsSourceTarget(graph):
    end = len(graph) - 1
    results = []

    def backtrack(start, path):
        if start == end:
            results.append(list(path))
            return
        for nextNode in graph[start]:
            path.append(nextNode)
            backtrack(nextNode, path)
            path.pop()

    path = deque([0])
    print(path)
    backtrack(0, path)

    return results

print(allPathsSourceTarget([[1,2],[3],[3],[]]))
graph = [[1,2],[3],[3],[]]
print(graph[0])