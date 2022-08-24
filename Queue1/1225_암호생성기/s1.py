import sys

sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    queue = list(map(int, input().split()))

    # n 초깃값 1
    n = 1
    while True:
        num = queue.pop(0)
        num -= n
        # 0보다 작거나 같으면? 0을 추가하고 break
        if num <= 0:
            queue.append(0)
            break
        queue.append(num)
        # 한 싸이클 == 5
        n %= 5
        n += 1

    print(f'#{t}', *queue)
