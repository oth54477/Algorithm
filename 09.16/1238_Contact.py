# 1238. Contact


from collections import deque


# def bfs(num):
#     visited = [False] * n
#     visited[arr.index(num)] = True
#     v = [num, 1]
#     queue = deque([v])
#     result = {}
#     while queue:
#         num, cnt = queue.popleft()
#         if cnt in result:
#             result[cnt] += [num]
#         else:
#             result[cnt] = [num]
#         for next_num in graph[num]:
#             visit = visited[arr.index(next_num)]
#             if not visit:
#                 if next_num not in keys:
#                     if cnt + 1 in result:
#                         result[cnt + 1] += [next_num]
#                     else:
#                         result[cnt + 1] = [next_num]
#                 else:
#                     visited[arr.index(next_num)] = True
#                     queue.append([next_num, cnt + 1])

#     print(result)
#     return max(result[list(result.keys())[-1]])


# for t in range(1, 11):
#     n, sp = map(int, input().split())
#     arr = list(map(int, input().split()))
#     graph = {}
#     for idx in range(0, n, 2):
#         from_node = arr[idx]
#         to_node = arr[idx + 1]
#         if from_node in graph:
#             graph[from_node] += [to_node]
#         else:
#             graph[from_node] = [to_node]
#     keys = graph.keys()
#     idx_table = list(keys)
#     print(graph)
#     print(f'#{t} {bfs(sp)}')

from collections import deque


def bfs(num):
    visited = [False] * 101
    visited[num] = True
    v = [num, 1]
    queue = deque([v])
    result = {}
    while queue:
        num, cnt = queue.popleft()
        if cnt in result:
            result[cnt] += [num]
        else:
            result[cnt] = [num]
        for next_num in graph[num]:
            if not visited[next_num]:
                visited[next_num] = True
                queue.append([next_num, cnt + 1])
    return max(list(result.values())[-1])


for t in range(1, 11):
    n, sp = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for idx in range(0, n, 2):
        graph[arr[idx]].append(arr[idx + 1])
    print(f'#{t} {bfs(sp)}')
