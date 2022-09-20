# 1861. 정사각형 방


# def dfs(row, col):
#     visited[row][col] = True
#     result[room] += 1

#     for i in range(4):
#         nr, nc = row + dr[i], col + dc[i]
#         if (
#             0 <= nr < n
#             and 0 <= nc < n
#             and not visited[nr][nc]
#             and (arr[row][col] + 1 == arr[nr][nc])
#         ):
#             dfs(nr, nc)


# from collections import deque


# def bfs(row, col):
#     cnt = 1
#     v = [row, col, cnt]
#     visited[row][col] = True
#     # result[room] += 1
#     queue = deque([v])

#     while queue:
#         row, col, cnt = queue.popleft()
#         for i in range(4):
#             nr, nc = row + dr[i], col + dc[i]
#             if (
#                 0 <= nr < n
#                 and 0 <= nc < n
#                 and not visited[nr][nc]
#                 and (arr[row][col] + 1 == arr[nr][nc])
#             ):
#                 visited[nr][nc] = True
#                 queue.append([nr, nc, cnt + 1])
#     return cnt


# rst = []
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# for t in range(1, int(input()) + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     result = [0] * (n**2 + 1)
#     breaker = False
#     for row in range(n):
#         if breaker:
#             break
#         for col in range(n):
#             visited = [[False] * n for _ in range(n)]
#             room = arr[row][col]
#             # dfs(row, col)
#             cnt = bfs(row, col)
#             result[room] = cnt
#             if result[-1] == (n**2):
#                 breaker = True
#                 break
#     max_room = max(result)
#     # print(f'#{t} {result.index(max_room)} {max_room}')

#     rst.append(f'#{t} {result.index(max_room)} {max_room}')
# print(*rst, sep='\n')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [0] * (n**2 + 1)

    for row in range(n):
        for col in range(n):
            room = arr[row][col]
            cnt = 1
            while True:
                for i in range(4):
                    nr, nc = row + dr[i], col + dc[i]
                    if 0 <= nr < n and 0 <= nc < n and arr[row][col] + 1 == arr[nr][nc]:
                        row, col = nr, nc
                        cnt += 1
                        break
                else:
                    result[room] = cnt
                    break

    max_room = max(result)
    print(f'#{t} {result.index(max_room)} {max_room}')
