import math
# 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # 경로 압축(Path compression)
    return parent[node]

for t in range(1, int(input()) + 1):
    n = int(input())    # 섬의 개수
    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))
    e = float(input())
    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = math.sqrt(((x_arr[i]-x_arr[j])**2 + (y_arr[i]-y_arr[j])**2))
                w = (distance**2) * e
                edges.append((w, i, j))

    edges.sort()  # (중요) 최소 비용의 간선부터 차례로 검사하기 위해 비용을 기준으로 오름차순 정렬
    parent = list(range(n + 1))
    counts = 0  # MST의 간선 개수 (정점 - 1 개가 되면 종료를 하기 위함)
    cost = 0  # MST의 가중치 총합(== 최소 비용)
    for dist, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)  # x와 y의 각각 대표값

        if x_root != y_root:  # 사이클이 아니면
            parent[y_root] = x_root  # union
            cost += dist
            counts += 1

            if counts >= n - 1:  # 간선의 최대 개수는 정점 - 1 이므로 break
                break
                
    print(f'#{t} {int(round(cost,0))}')