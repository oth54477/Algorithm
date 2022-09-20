import sys

sys.stdin = open('sample_input.txt')


def bfs(r, c):
    # 출발 위치 방문한 것으로 표시
    visited[r][c] = True
    # 큐에는 [row, col, 이동 거리]가 저장된다.
    queue = [[r, c, 0]]
    while queue:
        # dequeue를 통해 r, c, cnt 반환
        r, c, cnt = queue.pop(0)
        # 상 하 좌 우 델타이동
        for d in range(4):
            # 다음 위치 찾기
            nr, nc = r + dy[d], c + dx[d]
            # 범위 안에있고, 방문하지 않았다면
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                # 값이 0일 때 방문 표시, 큐에 enqueue
                if maze[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append([nr, nc, cnt + 1])
                # 값이 3일때 도착 -> return
                elif maze[nr][nc] == 3:
                    return cnt


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for t in range(1, int(input()) + 1):
    n = int(input())

    maze = [list(map(int, input())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]

    # 시작점 찾기
    for row in range(n):
        for col in range(n):
            if maze[row][col] == 2:
                result = bfs(row, col)
                # 도착점을 찾지 못해 None가 반환되면 0출력
                if result == None:
                    print(f'#{t} 0')
                # 이동 거리 출력
                else:
                    print(f'#{t} {result}')
