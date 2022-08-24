import sys

sys.stdin = open('input.txt')


def bfs(v):
    global depth
    if not visited[v]:
        visited[v] = True
        print(f'-{v}', end='')
        queue.pop(0)
        for q in path[v]:
            if not visited[q]:
                queue.append(q)
        if not queue:
            return
        bfs(queue[0])


n, m = map(int, input().split())

path = [[] for _ in range(n + 1)]
arr = list(map(int, input().split()))
for i in range(m):
    v1 = arr[i * 2]
    v2 = arr[i * 2 + 1]
    path[v1].append(v2)
    path[v2].append(v1)
depth = 0
visited = [False] * (n + 1)
queue = [1]
bfs(1)
