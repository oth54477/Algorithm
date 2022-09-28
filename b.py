from itertools import combinations

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for food in combinations(range(n), n // 2):
        taste_a, taste_b = 0, 0
        tmp = []
        for i in range(n):
            if i not in food:
                tmp.append(i)
        for row, col in combinations(food, 2):
            taste_a += arr[row][col] + arr[col][row]

        for r, c in combinations(tmp, 2):
            taste_b += arr[r][c] + arr[c][r]

        result.append(abs(taste_a - taste_b))

    print(f'#{t} {min(result)}')
