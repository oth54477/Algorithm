for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_f = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sum_f = 0
            for row in range(i, m + i):
                for col in range(j, m + j):
                    sum_f += arr[row][col]
            if max_f < sum_f:
                max_f = sum_f

    print(f'#{t} {max_f}')
