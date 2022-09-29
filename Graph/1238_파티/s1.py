import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start):
    distance[start] = 0                                     # 출발 위치 까지의 최단 거리 -> 0
    heap = [(0, start)]                                     # 힙 선언 [(비용, 정점)]

    while heap:                                             # 힙에 값이 있는 동안 반복
        min_dist, min_node = heappop(heap)                  # heap의 특징을 활용해 최단 거리가 가장 짧은 정점 선택

        if min_dist > distance[min_node]:                   # 이미 최단 거리로 기록되어 있는 값보다 큰 경우 무시
            continue

        for next_node, dist in graph[min_node]:             # 그래프에서 현재 정점에서 갈 수 있는 도착 정점 및 가중치 받아오기
            new_dist = min_dist + dist                      # 가중치 누적
            if new_dist < distance[next_node]:              # 저장된 값보다 누적값이 작을 때
                distance[next_node] = new_dist              # 값 갱신
                heappush(heap, (new_dist, next_node))       # heap에 추가


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]                            # 그래프
INF = 999999999                                             # 나올 수 없는 임의의 큰 수

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))                                 # 출발 위치를 인덱스로 (도착, 가중치) 저장
    
result = [0] * (n + 1)
for i in range(1, n+1):
    distance = [INF] * (n + 1)                              # 출발 정점에서 다른 정점들까지의 최단 거리 (무한으로 초기화)
    dijkstra(i)                                             # 다익스트라
    if i == x:                                              # 돌아가는 경우
        result = [x + y for x, y in zip(result, distance)]  # 리스트 끼리 더해주기
    else:                                                   # 가는 길
        result[i] += distance[x]                            # 목적지 까지의 최단 경로 더해주기
    
print(max(result[1:]))
        