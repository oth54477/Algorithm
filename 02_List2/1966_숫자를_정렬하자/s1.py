for t in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    # sorted 사용
    # print(f'#{t}', end=' ')
    # print(*(sorted(arr)))

    # 선택정렬 활용
    # 정렬된 원소는 고정
    for i in range(n - 1):
        min_num = 50
        for idx in range(i, n):
            # 최소값 찾기
            if min_num > arr[idx]:
                min_num, min_idx = arr[idx], idx
        # 최소값을 맨 앞으로 이동해주기
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f'#{t}', end=' ')
    print(*arr)
