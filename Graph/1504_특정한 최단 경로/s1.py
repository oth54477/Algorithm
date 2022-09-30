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
    graph[s].append((e, w))             # 양방향 길이 존재     
    graph[e].append((s, w))             # 양방향 길이 존재
v1, v2 = map(int, input().split())      # 반드시 거쳐야 하는 두 개의 서로 다른 정점 

distance = [INF] * (n + 1)              # distance 초기화
dijkstra(1)                             # 1에서 출발
d1_1, d1_2 = distance[v1], distance[v2] # v1으로 가는 최단 경로, v2로 가는 최단 경로
distance = [INF] * (n + 1)              # distance 초기화
dijkstra(v1)                            # v1에서 출발
d2_1, d2_2 = distance[v2], distance[n]  # v2로 가는 최단 경로, n으로 가는 최단 경로
distance = [INF] * (n + 1)              # distance 초기화
dijkstra(v2)                            # v2에서 출발
d3_1, d3_2 = distance[n], distance[v1]  # n으로 가는 최단 경로, v1으로 가는 최단 경로

result = min(d1_1 + d2_1 + d3_1, d1_2 + d2_2 + d3_2)    # 1 -> v1 -> v2 -> n, 1 -> v2 -> v2 -> n 중 더 최단 경로
if result >= INF:                       # 길이 없는 경우
    result = -1                         
print(result)