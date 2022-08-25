import sys

sys.stdin = open('sample_input.txt')


def find_path(row, col):
    global find_status
    visited[row][col] = True
    for d in range(4):
        nr, nc = row + dx[d], col + dy[d]
        # 도착 지점 에 도착했을 때
        if 0 <= nr < n and 0 <= nc < n and not find_status:
            if maze[nr][nc] == 3:
                find_status = True
                return
            # 범위 내에서 방문하지 않았고, 이동위치가 0이고, 아직 도착하지 못했을 때
            elif not visited[nr][nc] and maze[nr][nc] == 0:
                # 길 찾기
                find_path(nr, nc)


# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for t in range(1, int(input()) + 1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    find_status = False
    error_check = 0

    for r in range(n):
        if 2 in maze[r]:
            start_point = maze[r].index(2)
            # 길 찾기
            find_path(r, start_point)

            error_check += 1
        if 3 in maze[r]:
            error_check += 1
    # 2와 3이 각각 하나씩 존재하지 않을 경우 error 출력
    if error_check != 2:
        print(f'#{t} error')
    elif find_status:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
