# import sys

# sys.stdin = open('input.txt')


def pascal(stack):
    global n
    if len(stack) == n:
        return
    old_num = 0
    top = len(stack)
    while top < 0:
        if top == 0:
            now_num = 0
        else:
            now_num = stack.pop()
        top -= 1
        new_stack.append(old_num + now_num)
        old_num = now_num
    print(*new_stack)
    pascal(new_stack)


for t in range(1, int(input()) + 1):
    print(f'#{t}')
    print(1)
    n = int(input())
    if n == 1:
        continue

    stack = [1]
    new_stack = []
    pascal(stack)
