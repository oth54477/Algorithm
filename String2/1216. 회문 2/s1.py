for _ in range(10):
    t = input()
    # n x n 배열
    n = 100
    breaker = False
    # 문자열을 그대로 리스트에 저장
    arr = [input() for _ in range(n)]
    arr_col = [''] * n
    # 세로열을 리스트에 저장
    for row in range(n):
        for col in range(n):
            arr_col[row] += arr[col][row]

    for m in range(100, 0, -1):
        if breaker == True:
            break
        for row in range(n):
            if breaker == True:
                break
            # 검사할 구간을 슬라이싱 하기 위한 인덱스 idx
            for idx in range(n - m + 1):
                # 가로열 검사
                check_row = arr[row][idx : idx + m]
                # 세로열 검사
                check_col = arr_col[row][idx : idx + m]
                if (check_row == check_row[::-1]) or (check_col == check_col[::-1]):
                    print(f'#{t} {m}')
                    breaker = True
                    break
