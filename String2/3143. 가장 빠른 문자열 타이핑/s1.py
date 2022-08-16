for t in range(1, int(input()) + 1):
    a, b = map(str, input().split())
    # a안의 b 개수를 구한다.
    cnt = a.count(b)
    # a에서 b를 지운다.
    a = a.replace(b, '')
    # 나머지 글자의 길이를 구한다.
    cnt += len(a)
    print(f'#{t} {cnt}')
