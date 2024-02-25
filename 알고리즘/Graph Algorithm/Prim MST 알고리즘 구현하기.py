import heapq
import math

def prim(G, n):
    cost = [math.inf] * n
    parent = [None] * n
    visited = [False] * n
    cost[0] = 0 # 시작노드의 비용을 0으로 설정함

    #(비용,노드) 튜플로 구성된 힙 생성
    Q = [(cost[i], i) for i in range(n)]
    heapq.heapify(Q)

    while Q:
        # 최소비용의 노드 뽑아냄
        _, u = heapq.heappop(Q) # 아무런 값을 주지 않기 위해 _ 사용
        visited[u] = True
        # u에 인접한 모든 노드 v에 대해 for문 반복
        for v, weight in G[u]:
            if not visited[v] and weight < cost[v]:
                # v의 비용을 업데이트하고 부모를 설정
                cost[v] = weight
                parent[v] = u
                # 업데이트를 위해 새로운 (비용,노드)를 추가함
                heapq.heappush(Q, (weight, v))
    return sum(cost)

n = int(input())
m = int(input())  
G = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())  
    G[u].append((v, w))  
    G[v].append((u, w))

min_cost = prim(G, n)
print(min_cost)


'''
리스트와 Heap이라는 자료구조를 사용했다. 
이 코드의 시간 복잡도는 에지의 개수를 E, 노드의 개수를 V라 할 때, O((E+V) log V).이다. 
'''