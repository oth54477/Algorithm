# 1504. 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    distance[start].add(0)
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        for next_node, dist in graph[min_node]:
            while True:
                if len(distance[next_node]) <= k:
                    break
                distance[next_node] -= {max(distance[next_node])}
            new_dist = min_dist + dist
            if new_dist < max(distance[next_node]):
                distance[next_node].add(new_dist)
                heappush(heap, (new_dist, next_node))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 99999999999
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))             # 양방향 길이 존재     

distance = [{INF} for _ in range(n + 1)]              # distance 초기화
dijkstra(1)                             # 1에서 출발

result = -1
for path in distance[1:]:
    l = len(path)
    if l >= k:
        result = sorted(path)[k-1]
        if result >= 99999999999:
            result = -1
    print(result)