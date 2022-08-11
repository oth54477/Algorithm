t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = len(arr)
    result, count = 0, 0

    for i in range(1, 1 << n):  # n의 제곱만큼 반복
        for j in range(n):
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                count += arr[j]
        if count == 0:
            result = 1
        count = 0
    print(f'#{tc} {result}')
