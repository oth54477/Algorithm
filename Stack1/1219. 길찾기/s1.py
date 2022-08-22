import sys

sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


for _ in range(10):
    t, n = map(int, input().split())
    # 인접 리스트 생성
    graph = [[] for _ in range(100)]

    roads = list(map(int, input().split()))
    # 2개씩 처리
    for idx in range(0, 2 * n, 2):
        graph[roads[idx]].append(roads[idx + 1])

    # 방문처리 리스트
    visited = [False] * (100)

    dfs(0)
    print(f'#{t}', end=' ')
    if visited[99]:
        print(1)
    else:
        print(0)
