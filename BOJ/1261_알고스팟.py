# 1261_알고스팟
# https://www.acmicpc.net/problem/1261

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(row, col):
    distance[row][col] = 0
    heap = [(0, row, col)]

    while heap:
        min_dist, row, col = heappop(heap)

        if min_dist > distance[row][col]:
            continue

        for r, c in d:
            nr, nc = row + r, col + c
            if 0 <= nr < n and 0 <= nc < m:
                if maze[nr][nc] == 1:
                    dist = 1
                else:
                    dist = 0
                new_dist = min_dist + dist
                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                    heappush(heap, (new_dist, nr, nc))



d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
m, n = map(int, input().split())
INF = 999999999
distance = [[INF] * (m) for _ in range(n)]
maze = [list(map(int, input().strip())) for _ in range(n)]
dijkstra(0, 0)
print(distance[n-1][m-1])