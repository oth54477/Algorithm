from heapq import heappush, heappop

def dijkstra(start):
    distance[start] = 0                                 # 출발 위치 까지의 최단 거리 -> 0
    heap = [(0, start)]                                 # 힙 선언 (비용, 정점)
    
    while heap:                                         # 힙에 값이 있는 동안 반복
        min_dist, min_node = heappop(heap)              # 최단 거리가 가장 짧은 정점 선택
        
        if min_dist > distance[min_node]:               # 이미 최단 거리로 기록되어 있는 값보다 큰 경우 무시
            continue
        for next_node, dist in graph[min_node]:         # 그래프에서 현재 정점에서 갈 수 있는 도착 정점 및 가중치 받아오기
            new_dist = min_dist + dist                  # 가중치 누적
            if new_dist < distance[next_node]:          # 저장된 값보다 누적값이 작을 때
                distance[next_node] = new_dist          # 값 갱신
                heappush(heap, (new_dist, next_node))   # heap에 추가

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    INF = 999999999
    distance = [INF] * (n + 1)
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        
    dijkstra(0)                                         # 0번째 위치에서 시작
    print(f'#{t} {distance[-1]}')                       # distance의 마지막 원소가 최종 위치까지의 최단 거리
