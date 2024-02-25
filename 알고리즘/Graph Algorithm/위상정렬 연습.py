from collections import deque

def topological_sort(n, m, edges):
    indegree = [0] * n
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    result = []
    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

sorted_nodes = topological_sort(n, m, edges)

print(" ".join(map(str, sorted_nodes)))