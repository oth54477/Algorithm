import sys

sys.stdin = open('sample_input.txt')


def charge_cnt(sp):
    global cnt, min_cnt, status, end_cnt
    # print('sp :', sp)
    # print('min :', min_cnt)
    # print('cnt :', cnt)
    # print('memo :', memo)

    if sp > end_point or cnt > min_cnt:
        return
    else:
        ep = sp + charge[sp]
        if ep == end_point:
            cnt += 1
            # if end_cnt > cnt:
            #     end_cnt = cnt
            if min_cnt > cnt:
                min_cnt = cnt
            # cnt -= 1
            return
        for new_sp in range(sp + 1, ep + 1):
            cnt += 1
            charge_cnt(new_sp)
            cnt -= 1
            # print(end_cnt)


for t in range(1, int(input()) + 1):
    charge = list(map(int, input().split()))
    n = charge[0]
    charge = charge[1:]
    end_point = n - 1
    status = True
    # memo = [0] * (n - 1)
    arr = [[] for _ in range(n)]
    cnt, min_cnt, end_cnt = -1, n, n
    for i in range(n - 1):
        arr[i].append(i + charge[i])
    charge_cnt(0)

    print(f'#{t} {min_cnt}')
