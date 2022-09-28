# 4366. 정식이의 은행업무
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd&categoryId=AWMeRLz6kC0DFAXd&categoryType=CODE&problemTitle=%EC%A0%95%EC%8B%9D&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
def ter(n):
    result = ''
    while n != 0:
        n, r = divmod(n, 3)
        result += str(r)
    return result[::-1]


for t in range(1, int(input()) + 1):
    binary = input()
    ternary = input()
    b_decimal = int(binary, 2)
    t_decimal = int(ternary, 3)
    ter_len = len(ternary)
    bins = [b_decimal ^ 1 << i for i in range(len(binary))]
    for b in bins:
        ter_str = ter(b)
        ter_str = '0' * (ter_len - len(ter_str)) + ter_str
        cnt = 0
        for idx in range(ter_len):
            if ternary[idx] != ter_str[idx]:
                cnt += 1
        if cnt == 1:
            result = b
            break

    print(f'#{t} {result}')

    # t_arr = list(map(int, ternary))
    # result = 0
    # for i in range(min(b_decimal, t_decimal), max(b_decimal, t_decimal) + 1):
    #     chk = b_decimal ^ i
    #     if format(chk, 'b').count('1') == 1:
    #         ter_str = ter(i)
    #         ter_arr = list(map(int, ter_str))
    #         cnt = 0
    #         for x, y in zip(t_arr, ter_arr):
    #             if x - y != 0:
    #                 cnt += 1
    #         if cnt == 1:
    #             result = i
    #             break

    # print(f'#{t} {result}')
