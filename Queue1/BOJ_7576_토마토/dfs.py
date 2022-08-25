# BOJ_7576. 토마토

import sys

input = sys.stdin.readline

m, n = map(int, input().split())
cnt = 0
box = [list(map(int, input().split())) for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while True:
    tomato_cnt = 0
    visited = [[False] * m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            if box[row][col] == 1 and visited[row][col] == False:
                # 인접 토마토 익히기
                for dr in d:
                    nr, nc = row + dr[0], col + dr[1]
                    if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0:
                        tomato_cnt += 1
                        box[nr][nc] = 1
                        visited[nr][nc] = True
    if tomato_cnt == 0:
        break
    cnt += 1

if 0 in list(map(lambda x: 0 if 0 in x else 1, box)):
    print(-1)
else:
    print(cnt)
