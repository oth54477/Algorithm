T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for idx in range(N):
        count = 0
        for height in arr[idx + 1:]:
            if arr[idx] > height:           # 다음 블록보다 길이가 길면 +1
                count += 1
        if count > result:                 # 최종 count가 result보다 크면 result = count
            result = count
    print(f'#{tc} {result}')
