from collections import deque                   # 덱 불러오기

def bfs(node):                                  # BFS
    visited[node] = True
    q = deque([node])                           # 덱 생성
    while q:                                    # q에 값이 있는 동안 반복
        node = q.popleft()
        result.append(node)
        for next_v in graph[node]:
            if not visited[next_v]:
                q.append(next_v)
                visited[next_v] = True

arr = list(map(int, input().split()))
last_node = max(arr)                            # 가장 큰 값이 정점의 개수
graph = [set() for _ in range(last_node + 1)]
visited = [False] * (last_node + 1)
result = []
for idx in range(0,len(arr) - 1, 2):            # 인덱스를 2씩 건너뛰며 반환
    graph[arr[idx]].add(arr[idx+1])             # 인접 리스트 만들기
    graph[arr[idx+1]].add(arr[idx])             # 무향 그래프이므로 반대의 경우도 인접 리스트에 입력
bfs(1)                                          # 시작 정점 1에서 BFS 시작
print(*result)