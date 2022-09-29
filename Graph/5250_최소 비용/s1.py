from heapq import heappop, heappush

def dijkstra(sr, sc):
    distance[sr][sc] = 0                                    # 출발 위치 까지의 최단 거리 -> 0
    heap = [(0, sr, sc)]                                    # 힙 선언 [(비용, 정점)]

    while heap:                                     
        min_dist, min_row, min_col = heappop(heap)          # heap의 특징을 활용해 최단 거리가 가장 짧은 정점 선택

        if min_dist > distance[min_row][min_col]:           # 이미 최단 거리로 기록되어 있는 값보다 큰 경우 무시
            continue
        
        for r, c in d:                                      # 델타이동
            nr, nc = min_row + r, min_col + c               # 다음 위치 (행, 열)
            if 0 <= nr < n and 0 <= nc < n:                 # 범위를 벗어나지 않으면
                dist = arr[nr][nc] - arr[min_row][min_col]  # 높이 차에 의한 연료 소모량 계산
                if dist < 0:                                # 높이 차에 의한 연료 소모량이 음수 이면
                    dist = 0                                # 연료 소모량 = 0
                dist += 1                                   # 기본 이동시 소모량 -> 1
                
                new_dist = min_dist + dist                  # 가중치 누적
                if new_dist < distance[nr][nc]:             # 저장된 값보다 누적값이 작을 때
                    distance[nr][nc] = new_dist             # 값 갱신
                    heappush(heap, (new_dist, nr, nc))      # heap에 추가

    
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]                      # 델타이동 (상, 하, 좌, 우)
for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    INF = 999999999                                         # 나올 수 없는 임의의 큰 수
    distance = [[INF] * n for _ in range(n)]                # 출발 정점에서 다른 정점들까지의 최단 거리 (무한으로 초기화)

    dijkstra(0, 0)                                          # 다익스트라
    print(f'#{t} {distance[n - 1][n - 1]}')                 # 오른쪽 맨 아래 값
