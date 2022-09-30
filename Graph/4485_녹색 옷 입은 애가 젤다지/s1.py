# 4485. 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(row, col):
    first_dist = cave[row][col]                             # 출발점의 도둑루피 크기
    distance[row][col] = first_dist
    heap = [(first_dist, row, col)]

    while heap:
        min_dist, row, col = heappop(heap)

        if min_dist > distance[row][col]:
            continue

        for r, c in d:
            nr, nc = row + r, col + c
            if 0 <= nr < n and 0 <= nc < n:
                dist = cave[nr][nc]                         # 다음 위치의 도둑루피 크기
                new_dist = min_dist + dist
                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                    heappush(heap, (new_dist, nr, nc))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = 0
while True:    
    n = int(input())
    t += 1
    if n == 0:
        break
    INF = 999999999
    distance = [[INF] * n for _ in range(n)]
    cave = [list(map(int, input().split())) for _ in range(n)]
    dijkstra(0, 0)
    print(f'Problem {t}: {distance[n - 1][n - 1]}')