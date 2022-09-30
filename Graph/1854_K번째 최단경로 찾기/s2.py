# 1816. 최소비용 구하기
# https://www.acmicpc.net/problem/1916
import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    distance[start].append(0)
    heap = [(0, start)]
    while heap:
        min_dist, min_node = heappop(heap)
        for next_node, dist in graph[min_node]:
            
            while True:
                if len(distance[next_node]) <= k:   
                    break
                distance[next_node].remove(max(distance[next_node]))
                
            new_dist = min_dist + dist
            if new_dist < max(distance[next_node]):
                distance[next_node].append(new_dist)
                heappush(heap, (new_dist, next_node))


n, m, k = map(int, input().split())                 # 도시의 개수, 도로 수, k 번째 
graph = [[] for _ in range(n + 1)]                  # 도로 정보를 저장할 그래프
INF = 999999999
distance = [[INF] for _ in range(n + 1)]            # 이동 시간을 저장할 리스트
for _ in range(m):                                  
    s, e, w = map(int, input().split())             # 출발, 도착, 이동 시간
    graph[s].append((e, w))                         # 그래프에 저장

dijkstra(1)                                         # 1번 도시에서 출발
result = -1
print(distance)
for path in distance[1:]:
    l = len(path)
    if l >= k:
        result = sorted(path)[k-1]
        if result >= 999999999:
            result = -1
    print(result)