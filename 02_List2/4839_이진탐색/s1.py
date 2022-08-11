def binary_search(p, target):
    count = 0
    l, r = 1, p
    while True:
        c = int((l + r) / 2)
        if l == c or l == r:
            return p
        count += 1
        if target < c:
            r = c
        elif target > c:
            l = c
        else:
            return count


for tc in range(1, int(input()) + 1):
    p, a, b = map(int, input().split())
    a_num = binary_search(p, a)
    b_num = binary_search(p, b)
    if a_num < b_num:
        winner = 'A'
    elif a_num > b_num:
        winner = 'B'
    else:
        winner = 0
    print(f'#{tc} {winner}')
