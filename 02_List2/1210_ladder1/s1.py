for _ in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 목표 지점의 열 변호 찾기
    goal = arr[99].index(2)
    r = [0, 0, -1]  # 왼 오 위
    c = [-1, 1, 0]

    # 시작위치 지정(목표 위치)
    row, col = 99, goal

    # 0 : 위, 1 : 왼쪽, 2: 오른쪽
    d = 0
    # row가 0보다 작을 때(범위를 벗어날 때)까지 반복
    while row >= 0:
        # 열이 범위를 벗어나지 않고, 직전에 오른쪽으로 이동하지 않았고, 1일때 왼쪽으로 이동
        if col > 0 and arr[row + r[0]][col + c[0]] != 0 and d != 2:
            row += r[0]
            col += c[0]
            d = 1
        # 열이 범위를 벗어나지 않고, 직전에 왼쪽으로 이동하지 않았고, 1일때 오른쪽으로 이동
        elif col < 99 and arr[row + r[1]][col + c[1]] != 0 and d != 1:
            row += r[1]
            col += c[1]
            d = 2
        # 왼쪽과 오른쪽이 모두 0이면 위로 이동
        else:
            row += r[2]
            col += c[2]
            d = 0
    # 시작 위치 출력
    print(f'#{t} {col}')
