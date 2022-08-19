# BOJ_10157. 자리배정

c, r = map(int, input().split())
k = int(input())
# 자리를 지정할 수 없는 경우 0
if c * r < k:
    print(0)
else:
    hall = [[0] * c for _ in range(r)]
    # 상, 우, 하, 좌 델타이동
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    number = 1
    # 시작 위치 지정
    nr, nc = r - 1, 0
    # 시작 방향 지정
    dr = 0
    while number < k + 1:
        # 범위 내에 있고, 0인경우
        if 0 <= nr < r and 0 <= nc < c and not hall[nr][nc]:
            hall[nr][nc] = number
            number += 1
            row, col = nr, nc
        else:
            dr += 1
        dr %= 4
        nr, nc = row + d[dr][0], col + d[dr][1]

    print(col + 1, r - row)
