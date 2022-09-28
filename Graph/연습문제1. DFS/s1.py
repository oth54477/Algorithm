def dfs(node):
    visited[node] = True
    result.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:              # 방문 x 일 때
            dfs(next_node)                      # 재귀

arr = list(map(int, input().split()))
last_node = max(arr)                            # 가장 큰 값이 정점의 개수
graph = [set() for _ in range(last_node + 1)]
visited = [False] * (last_node + 1)
result = []
for idx in range(0,len(arr) - 1, 2):            # 인덱스를 2씩 건너뛰며 반환
    graph[arr[idx]].add(arr[idx+1])             # 인접 리스트 만들기
    graph[arr[idx+1]].add(arr[idx])             # 무향 그래프이므로 반대의 경우도 인접 리스트에 입력
dfs(1)                                          # 시작 정점 1에서 DFS 시작
print(*result)