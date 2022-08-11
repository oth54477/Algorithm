for tc in range(10):
    t = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    diagonal_1, diagonal_2 = 0, 0
    result_arr = []
    for i in range(100):
        cols_sum = 0
        # 행의 합
        result_arr.append(sum(arr[i]))
        # 대각선 1의 합
        diagonal_1 += arr[i][i]
        # 대각선 2의 합
        diagonal_2 += arr[i][99 - i]
        for j in range(100):
            # 열의 합
            cols_sum += arr[j][i]
        result_arr.append(cols_sum)
    result_arr.append(diagonal_1)
    result_arr.append(diagonal_2)

    print(f'#{t} {max(result_arr)}')
