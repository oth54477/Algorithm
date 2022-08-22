import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(row, col):
    visited[row][col] = True
    # 델타이동하며 dfs
    for dr in d:
        nr, nc = row + dr[0], col + dr[1]
        if (
            (0 <= nr < m)
            and (0 <= nc < n)
            and (not visited[nr][nc])
            and (field[nr][nc] == 1)
        ):
            dfs(nr, nc)


d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(int(input())):
    m, n, k = map(int, input().split())

    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    for row in range(m):
        for col in range(n):
            # 값이 1이고, 방문한적 없으면 cnt += 1, dfs 시작
            if field[row][col] == 1 and (not visited[row][col]):
                cnt += 1
                dfs(row, col)
    print(cnt)
