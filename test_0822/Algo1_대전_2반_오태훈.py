for t in range(1, int(input()) + 1):
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(n)]

    # 높이들을 더하기 위한 sum_h 선언
    sum_h = 0
    # 평지로 만들려는 범위의 높이를 모두 더하기
    for row in range(r1, r2 + 1):
        for col in range(c1, c2 + 1):
            sum_h += land[row][col]
    # 더한 값을 넓이로 나눠 평균값 구하기
    avr_h = sum_h // ((r2 - r1 + 1) * (c2 - c1 + 1))
    sum_land = 0
    # 평지로 만들려는 범위의 높이에서 평탄화 높이를 빼기
    for row in range(r1, r2 + 1):
        for col in range(c1, c2 + 1):
            d = land[row][col] - avr_h
            # 절대값 구하기
            if d < 0:
                d = -d
            # 모두 더하기
            sum_land += d
    print(f'#{t} {sum_land}')