import sys

sys.stdin = open('sample_input.txt')


def charge_cnt(sp):
    global min_cnt, cnt, status
    ep = sp + charge[sp]
    if status:
        return

    if ep >= end_point:
        status = True
        return

    if cnt != 0 and min_cnt > cnt:
        min_cnt = cnt

    for np in range(sp + 1, ep + 1):
        cnt += 1
        charge_cnt(np)
        cnt -= 1


for t in range(1, int(input()) + 1):
    charge = list(map(int, input().split()))
    n, charge = charge[0], charge[1:]
    end_point = n - 1
    cnt = 0
    min_cnt = n
    status = False

    charge_cnt(0)

    print(min_cnt)
