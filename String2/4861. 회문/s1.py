for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    # 문자열을 그대로 리스트에 저장
    arr = [input() for _ in range(n)]
    # 세로열을 저장할 리스트 생성
    arr_col = [''] * n
    # 세로열을 리스트에 저장
    for row in range(n):
        for col in range(n):
            arr_col[row] += arr[col][row]
    # 검사
    for row in range(n):
        # 검사할 구간을 슬라이싱 하기 위한 인덱스 idx
        for idx in range(n - m + 1):
            # 가로열 검사
            check_row = arr[row][idx : idx + m]
            # 세로열 검사
            check_col = arr_col[row][idx : idx + m]
            if check_row == check_row[::-1]:
                print(f'#{t} {check_row}')
            elif check_col == check_col[::-1]:
                print(f'#{t} {check_col}')
