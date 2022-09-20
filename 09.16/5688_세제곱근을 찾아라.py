# 5688. 세제곱근을 찾아라

for t in range(1, int(input()) + 1):
    n = int(input())

    num = n ** (1 / 3)
    r_num = round(num)
    print(r_num)
    print(r_num**3)
    if r_num**3 == n:
        result = r_num
    else:
        result = -1
    print(f'#{t} {result}')
