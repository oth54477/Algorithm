for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    queue = list(map(int, input().split()))

    # print(f'#{t} {queue[m % n]}')
    for _ in range(m):
        queue.append(queue.pop(0))
    print(f'#{t} {queue[0]}')
