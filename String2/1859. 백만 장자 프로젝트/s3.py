import sys


sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    costs = list(map(int, input().split()))

    revenue = 0
    while True:
        # 가장 비싼 날 찾기
        max_cost = max(costs)
        max_idx = costs.index(max_cost)

        # 가장 비쌀때 팔기
        revenue += max_idx * max_cost - sum(costs[:max_idx])
        # 지금까지의 리스트 지우기
        del costs[: max_idx + 1]
        # 리스트가 비면 정지
        if not costs:
            break

    print(f'#{t} {revenue}')
