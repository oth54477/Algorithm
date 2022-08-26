# 6190. 정곤이의 단조 증가하는 수
def chk(num):
    list_num = list(str(num))
    for m in range(len(list_num) - 1):
        if list_num[m] > list_num[m + 1]:
            break
    else:
        return 1
    return 0


for t in range(1, int(input()) + 1):
    n = int(input())

    num_arr = list(map(int, input().split()))

    max_result = 0
    for i in range(n - 1):
        for j in range(n - 1, 0 + i, -1):
            chk_num = num_arr[i] * num_arr[j]
            if chk(chk_num) and max_result <= chk_num:
                max_result = chk_num
    if max_result != 0:
        print(f'#{t} {max_result}')
    else:
        print(f'#{t} -1')
