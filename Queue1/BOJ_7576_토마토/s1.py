from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    global cnt
    while queue:
        r, c, cnt = queue.popleft()
        cnt += 1
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0:
                box[nr][nc] = 1
                queue.append([nr, nc, cnt])


m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque([])
for row in range(n):
    for col in range(m):
        if box[row][col] == 1:
            queue.append([row, col, 0])

result = bfs()
# 0이 하나라도 있으면 (한 줄에 0 이 없으면 1, 있으면 0)
if sum(list(map(lambda x: 1 if 0 not in x else 0, box))) != n:
    print(-1)
    exit(0)
else:
    print(cnt - 1)
