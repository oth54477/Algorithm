# 3. 재귀 - 경로 압축(부모 노드를 대표값으로 만듦)
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # 정점, 간선(Union 횟수) 개수
    parent = list(range(n + 1))
    arr = list(map(int, input().split()))
    for idx in range(0, m * 2 - 1, 2):
        x, y = arr[idx], arr[idx + 1]
        x_root, y_root = find_set(x), find_set(y)  # Find
    
        # Union
        if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root
    for i in range(1, n+1):
        parent[i] = find_set(i)
    print(parent)
    print(f'#{t} {len(set(parent)) - 1}')