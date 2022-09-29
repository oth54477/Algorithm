# 1816. 최소비용 구하기
# https://www.acmicpc.net/problem/1916
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




n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
INF = 999999999
distance = [INF] * (n + 1)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())

dijkstra(start)
print(distance[end])