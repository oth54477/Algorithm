def bfs(v):
    pass


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())

    graph[v1].append(v2)
    graph[v2].append(v1)
    visited = [0] * (n + 1)

    for i in range(n):
        visited = [[False] * (n + 1)]
        bfs(i)

a = list(range(100000000000))
for 1 in a:
    print(1)