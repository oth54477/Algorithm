import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    costs = list(map(int, input().split()))

    start_idx, revenue = 0, 0
    while True:
        max_cost = max(costs[start_idx:])
        max_idx = start_idx + costs[start_idx:].index(max_cost)
        # for cost in costs[start_idx:max_idx]:
        #     revenue += max_cost - cost

        revenue += (max_idx - start_idx) * max_cost - sum(costs[start_idx:max_idx])
        start_idx = max_idx + 1
        if start_idx >= n:
            break

    print(f'#{t} {revenue}')
