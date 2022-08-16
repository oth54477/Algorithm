for t in range(1, int(input()) + 1):
    arr = [input() for _ in range(5)]
    # 문자열의 최대 길이는 15이므로 15칸 생성
    arr_col = [''] * 15
    for row in range(15):
        for col in range(5):
            # 해당 문자열의 길이가 찾고자 하는 위치보다 작으면 넘긴다.
            if len(arr[col]) <= row:
                continue
            arr_col[row] += arr[col][row]

    result = ''.join(arr_col)
    print(f'#{t} {result}')
