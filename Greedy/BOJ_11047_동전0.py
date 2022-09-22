n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)][::-1]

cnt = 0
for money in arr:
    if k == 0:
        break
    if money <= k:
        cnt += k // money
        k %= money
print(cnt)