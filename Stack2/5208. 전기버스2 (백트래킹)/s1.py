import sys

sys.stdin = open('sample_input.txt')


def charge_cnt(v):
    global cnt
    cnt += 1
    print(v)
    move = v + charge[v]
    if move == end_point:
        return
    else:

        charge_cnt(move)


for t in range(1, int(input()) + 1):
    charge = list(map(int, input().split()))
    n = charge[0]
    charge = charge[1:]
    end_point = n - 1

    visited = [False] * end_point

    arr = [[] for _ in range(n)]
    cnt = 0
    for i in range(n - 1):
        arr[i].append(i + charge[i])

    charge_cnt(0)

    print(cnt)
