def paper(n):
    if len(memo) <= n and n > 2:
        # 점화식 p(n) = p(n-1) + p(n-2) * 2
        memo.append(paper(n - 1) + paper(n - 2) * 2)
    return memo[n - 1]


for t in range(1, int(input()) + 1):
    n = int(input())
    memo = [1, 3]
    print(f'#{t}', paper(n // 10))
