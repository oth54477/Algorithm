for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_count = 0
    count = 0
    for row in range(n):
        count = 0
        for col in range(m):
            # 가로 탐색
            if arr[row][col] == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0
        if max_count < count:
            max_count = count

    for col in range(m):
        count = 0
        for row in range(n):
            # 세로 탐색
            if arr[row][col] == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0

        if max_count < count:
            max_count = count

    print(f'#{t} {max_count}')
