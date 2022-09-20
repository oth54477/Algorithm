# 10726. 이진수 표현
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS&categoryId=AXRSXf_a9qsDFAXS&categoryType=CODE&problemTitle=10726&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    m = format(m, 'b')
    result = 'ON'
    if n > len(m):
        result = 'OFF'
    else:
        if '0' in m[-n:]:
            result = 'OFF'
    print(f'#{t} {result}')
    # cnt, result = 0, 'OFF'
    # if n <= len(m):
    #     for i in m[::-1]:
    #         if cnt == n:
    #             break
    #         if i == '0':
    #             result = 'OFF'
    #             break
    #         else:
    #             result = 'ON'
    #         cnt += 1

    # print(f'#{t} {result}')
