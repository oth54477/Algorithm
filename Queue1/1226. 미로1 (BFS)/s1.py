import sys

sys.stdin = open('input.txt')


def bfs(r, c):
    visited[r][c] = True
    queue = [[r, c]]

    while queue:
        r, c = queue.pop(0)
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                if maze[nr][nc] == 3:
                    return 1
                queue.append([nr, nc])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(10):
    t = int(input())

    maze = [list(map(int, input())) for _ in range(16)]

    sr, sc = 1, 1

    visited = [[False] * 16 for _ in range(16)]

    result = bfs(sr, sc)

    if result != None:
        print(f'#{t} {result}')
    else:
        print(f'#{t} 0')
