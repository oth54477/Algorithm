# 13549. 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)
        if min_dist > distance[min_node]:
            continue
        for d in range(3):
            if d == 0:
                next_node = min_node + 1
                dist = 1
            elif d == 1:
                next_node = min_node - 1
                dist = 1
            else:
                next_node = min_node * 2
                dist = 0
            if not 0 <= next_node <= 100000:
                continue
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, k = map(int, input().split())
distance = [999999999] * 100001
dijkstra(n)
print(distance[k])