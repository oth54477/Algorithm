for t in range(1, int(input()) + 1):

    n = int(input())

    arr = [[0] * 10 for _ in range(10)]
    count = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        # row에 y1 ~ y2까지 할당
        for row in range(y1, y2 + 1):
            # col에 x1 ~ x2 까지 할당
            for col in range(x1, x2 + 1):
                # 깂이 color와 같지 않고, 3보다 작으면 color을 더하기
                if arr[row][col] != color and arr[row][col] < 3:
                    arr[row][col] += color
    for row in range(10):
        count += arr[row].count(3)
    print(f'#{t} {count}')
