for t in range(1, 11):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    sum_num = 0
    for row in range(n):
        for col in range(n):
            for d in range(4):
                nr, nc = row + dy[d], col + dx[d]

                if 0 <= nr < n and 0 <= nc < n:
                    num = arr[nr][nc] - arr[row][col]
                    if num < 0:
                        num = -num
                    sum_num += num

    print(f'#{t} {sum_num}')
