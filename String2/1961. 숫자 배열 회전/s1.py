for t in range(1, int(input()) + 1):
    n = int(input())

    arr = [list(map(str, input().split())) for _ in range(n)]
    # zip 함수를 활용해 회전
    arr_90 = list(map(list, zip(*arr[::-1])))
    arr_180 = list(map(list, zip(*arr_90[::-1])))
    arr_270 = list(map(list, zip(*arr_180[::-1])))
    print(f'#{t}')
    for idx in range(n):
        print(''.join(arr_90[idx]), end=' ')
        print(''.join(arr_180[idx]), end=' ')
        print(''.join(arr_270[idx]), end=' ')
        print()
