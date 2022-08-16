# 9386. 연속한 1의 개수

for tc in range(1, int(input()) + 1):
    n = int(input())
    sequence = int(input())

    for i in range(1<<n, 0,-1):
        