# 1486. 장훈이의 높은 선반

from itertools import combinations

for t in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    people = list(map(int, input().split()))

    subset = []
    for i in range(n + 1):
        subset += list(combinations(people, i))
    result = []
    for p in subset:
        num = sum(p)
        if num >= b:
            result.append(num)

    print(f'#{t} {min(result) - b}')
