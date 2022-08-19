# 3499. 퍼펙트 셔플

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(str, input().split()))
    if n % 2 == 0:
        stack1, stack2 = arr[: n // 2], arr[n // 2 :]
    else:
        stack1, stack2 = arr[: n // 2 + 1], arr[n // 2 + 1 :]

    result = []
    for i in range(0, n, 2):
        if stack1:
            result.append(stack1.pop(0))
        if stack2:
            result.append(stack2.pop(0))

    print(f'#{t}', *result)
