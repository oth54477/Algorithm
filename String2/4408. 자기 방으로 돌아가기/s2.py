for t in range(1, int(input()) + 1):
    n = int(input())
    cnt = 1
    rooms = [0] * 200
    for _ in range(n):
        status = False
        start, end = map(int, input().split())
        if start % 2 == 0:
            start -= 1
        if end % 2 == 0:
            end -= 1
        if start <= end:
            move = range(start // 2 + 1, end // 2 + 2)
        else:
            move = range(end // 2 + 1, start // 2)
        for idx in move:
            if status == False and rooms[idx] != 0:
                cnt += 1
                status = True
            rooms[idx] += 1
    print(f'#{t} {cnt}')
