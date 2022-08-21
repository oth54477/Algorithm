import sys

sys.stdin = open('input.txt')


def pascal(stack):
    global n
    new_stack = []
    old_num = 0
    # stack이 빈경우 -> [1] (n이 1)
    if not stack:
        new_stack = [1]
    else:
        for _ in range(len(stack) + 1):
            if not stack:
                now_num = 0
            else:
                now_num = stack.pop()
            new_stack.append(old_num + now_num)
            old_num = now_num

    print(*new_stack)
    if len(new_stack) >= n:
        return
    else:
        pascal(new_stack)


for t in range(1, int(input()) + 1):
    print(f'#{t}')
    n = int(input())

    stack = []
    pascal(stack)
