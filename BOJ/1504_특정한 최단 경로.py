# 1504. 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

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

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))




n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = 999999999
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
v1, v2 = map(int, input().split())

distance = [INF] * (n + 1)
dijkstra(1)
d1_1 = distance[v1]
d1_2 = distance[v2]
distance = [INF] * (n + 1)
dijkstra(v1)
d2_1 = distance[v2]
d2_2 = distance[n]

distance = [INF] * (n + 1)
dijkstra(v2)
d3_1 = distance[n]
d3_2 = distance[v1]

result = min(d1_1 + d2_1 + d3_1, d1_2 + d2_2 + d3_2)
if result >= INF:
    result = -1
print(result)