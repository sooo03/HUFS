def Kruskal(V, E):
    # 원소가 하나인 경우의 집합을 초기화함
    def make_set(v):
        parent[v] = v
        rank[v] = 0

    # 집합의 대표를 찾음
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    # 랭크를 사용하여 두 집합을 합침
    def union(root1, root2):
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            rank[root2] += 1

    T = [] # 최소 신장 트리의 간선을 저장할 리스트
    parent = {} # 각 정점의 부모를 저장할 딕셔너리
    rank = {} # 각 집합의 랭크를 저장할 딕셔너리 (랭크 기반 합집합을 위해 사용)

    # 각 정점을 독립된 집합으로 초기화
    for v in V:
        make_set(v)

    # 에지 리스트 E를 가중치 기준으로 오름차순으로 정렬
    E.sort(key=lambda edge: edge[2])

    # 정렬된 에지 순회
    for edge in E:
        u, v, weight_uv = edge
        root_u = find(u)
        root_v = find(v)
        # 에지를 추가해도 사이클이 생성되지 않는 경우
        if root_u != root_v:
            # 에지를 최소 신장 트리에 추가
            T.append(edge)
            # root_u와 root_v를 통합
            union(root_u, root_v)
    return T


V = list(range(int(input())))
E = [list(map(int, input().split())) for _ in range(int(input()))]

minimum_spanning_tree = Kruskal(V, E)
total_weight = sum(edge[2] for edge in minimum_spanning_tree)

print(total_weight)

'''
G의 MST를 계산하면서 E의 에지는 가중치의 오름차순으로 이미 정렬되어 있다고 가정했다. 에지 (u,v)가 질의로 주어지면, LCA(u,v)=p를 계산하고, u에서 p 경로에 있는 최대 weight 값과 v에서 p까지의 최대 weight 값을 O(logn) 시간에 알려준다. 따라서 이 알고리즘은 O(logn) 시간에 수행 가능하다.
'''