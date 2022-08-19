# 7465. 창용 마을 무리의 개수
def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    cnt = 0
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == False:
            cnt += 1
            dfs(i)

    print(f'#{t} {cnt}')
