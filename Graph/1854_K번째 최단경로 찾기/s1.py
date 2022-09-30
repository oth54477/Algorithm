# 1816. 최소비용 구하기
# https://www.acmicpc.net/problem/1916
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    distance[start] = {0}
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
INF = 999999999
distance = [{INF} for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)
print(distance)
result = -1
for path in distance[1:]:
    l = len(path)
    if l == 1 and list(path)[0] == INF:
        pass
    elif l >= k:
        result = sorted(path)[k-1]
    print(result)

