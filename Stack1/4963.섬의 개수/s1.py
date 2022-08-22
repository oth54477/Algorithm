import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(row, col):
    visited[row][col] = True
    # 델타이동하며 dfs
    for dr in d:
        nr, nc = row + dr[0], col + dr[1]
        if (
            (0 <= nr < h)
            and (0 <= nc < w)
            and (not visited[nr][nc])
            and (field[nr][nc] == 1)
        ):
            dfs(nr, nc)

# 8방향 설정
d = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    field = [list(map(int, input().split())) for _ in range(h)]

    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for row in range(h):
        for col in range(w):
            # 값이 1이고, 방문한적 없으면 cnt += 1, dfs 시작
            if field[row][col] == 1 and (not visited[row][col]):
                cnt += 1
                dfs(row, col)
    print(cnt)
