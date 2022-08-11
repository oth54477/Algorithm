for t in range(1, int(input()) + 1):
    n = int(input())

    arr = list(map(int, input().split()))

    arr_sort = sorted(arr)
    arr_reverse = sorted(arr, reverse=True)

    result = []
    for i in range(n // 2):
        # 결과가 10이되면 정지
        if len(result) == 10:
            break
        # 오름자순의 값과 내림차순의 값이 같으면 한번만 추가하고 정지
        elif arr_reverse[i] == arr_sort[i]:
            result.append(arr_sort[i])
            break
        result.append(arr_reverse[i])
        result.append(arr_sort[i])
    print(f'#{t}', end=' ')
    print(*result)
