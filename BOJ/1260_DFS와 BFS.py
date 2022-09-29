# 1260. DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def dfs(node):
    visited[node] = True
    dfs_arr.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

def bfs(node):
    visited[node] = True
    q = deque([node])
    while q:
        node = q.popleft()
        bfs_arr.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)


input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for i in range(n+1):
    graph[i].sort()
dfs_arr, bfs_arr = [], []
visited = [False] * (n + 1)
dfs(v)
visited = [False] * (n + 1)
bfs(v)
    
print(*dfs_arr)
print(*bfs_arr)
