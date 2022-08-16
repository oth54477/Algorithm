# 1859. 백만 장자 프로젝트
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    costs = list(map(int, input().split()))
    income, before_index = 0, 0
    for cost_index, cost_value in enumerate(costs[:-1]):
        # 다음 가격이 줄어드는 경우
        if cost_value >= costs[cost_index + 1]:
            # 이전 위치 부터 차액 더하기
            for value in costs[before_index:cost_index]:
                sale = costs[cost_index] - value
                if sale > 0:
                    income += sale
            before_index = cost_index
    for value in costs[before_index:]:
        sale = costs[-1] - value
        if sale > 0:
            income += sale
    print(f'#{test_case} {income}')
