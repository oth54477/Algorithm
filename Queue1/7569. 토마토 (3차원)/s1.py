from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    global cnt
    while queue:
        r, c, h, cnt = queue.popleft()
        cnt += 1
        for d in range(6):
            nr, nc, nh = r + dy[d], c + dx[d], h + dz[d]
            if 0 <= nr < n and 0 <= nc < m and 0 <= nh < k and box[nh][nr][nc] == 0:
                box[nh][nr][nc] = 1
                queue.append([nr, nc, nh, cnt])


m, n, k = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(k)]

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque([])
for height in range(k):
    for row in range(n):
        for col in range(m):
            if box[height][row][col] == 1:
                queue.append([row, col, height, 0])

result = bfs()
# 0이 하나라도 있으면 (한 줄에 0 이 없으면 1, 있으면 0)
# if sum(list(map(lambda x: 1 if 0 not in x else 0, box))) != n:
if (
    sum(list(map(lambda x: sum(list(map(lambda x: 1 if 0 not in x else 0, x))), box)))
    != n * k
):
    print(-1)
    exit(0)
else:
    print(cnt - 1)
