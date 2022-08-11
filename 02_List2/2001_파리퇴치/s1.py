for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_fly = 0
    # 1로 가득찬 리스트 설정
    mask = [[1] * m for _ in range(m)]
    # 반복 횟수 설정
    k = n - m + 1
    for i in range(k):
        for col in range(k):
            sum_product = 0
            for row in range(m):
                # 리스트 곱
                arr_product = [
                    x * y for x, y in zip(arr[row + i][col : col + m], mask[0])
                ]
                sum_product += sum(arr_product)
            if max_fly < sum_product:
                max_fly = sum_product
    print(f'#{t} {max_fly}')
