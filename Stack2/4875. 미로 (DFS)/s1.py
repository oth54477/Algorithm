# import sys

# sys.stdin = open('sample_input.txt')


def find_path(row, col, depth):
    global find_status
    visited[row][col] = True
    cnt = 0
    for d in range(4):
        nr, nc = row + dx[d], col + dy[d]
        if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 3:
            print(f'#{t} 1')
            find_status = True
            return
        elif 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] == 0:
            path.append([nr, nc])
            find_path(nr, nc, depth + 1)
            if find_status:
                break
            path.pop()
        else:
            cnt += 1
    if cnt == 4:
        if depth == 1 or 0:
            print(f'#{t} 0')
        return


# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for t in range(1, int(input()) + 1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    path = []
    find_status = False
    error_check = 0
    for r in range(n):
        if 2 in maze[r]:
            start_point = maze[r].index(2)
            sr = r
            error_check += 1
        if 3 in maze[r]:
            error_check += 1
    if error_check != 2:
        print(f'#{t} error')
    else:
        find_path(sr, start_point, 0)
