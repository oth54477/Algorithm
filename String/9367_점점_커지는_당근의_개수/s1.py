for t in range(1, int(input()) + 1):
    n = int(input())
    cnt = 1
    old_cnt = 0
    c = list(map(int, input().split()))
    for i in range(1, n):
        if c[i - 1] < c[i]:
            cnt += 1
        else:
            if old_cnt < cnt:
                old_cnt = cnt
            cnt = 1
    if old_cnt > cnt:
        cnt = old_cnt
    print(f'#{t} {cnt}')
