t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    row_way = [-1, 1, 0, 0]  # 상 하 좌 우
    col_way = [0, 0, -1, 1]

    for row in range(n):
        for col in range(n):
            for i in range(4):
                r = row + row_way[i]
                c = col + col_way[i]
                if 0 <= r < n and 0 <= c < n:
                    result += abs(arr[r][c] - arr[row][col])
    print(f'#{tc} {result}')
