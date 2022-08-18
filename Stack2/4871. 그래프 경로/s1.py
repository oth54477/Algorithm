def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


for t in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    # 인접 리스트 생성
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        # 인접 리스트에 push
        graph[v1].append(v2)

    s, g = map(int, input().split())
    # 방문처리 리스트
    visited = [False] * (v + 1)

    dfs(s)
    print(f'#{t}', end=' ')
    if visited[g]:
        print(1)
    else:
        print(0)
