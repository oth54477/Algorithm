# 4366. 정식이의 은행업무
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWMeRLz6kC0DFAXd&categoryId=AWMeRLz6kC0DFAXd&categoryType=CODE&problemTitle=%EC%A0%95%EC%8B%9D&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
for t in range(1, int(input()) + 1):
    binary = input()
    ternary = input()
    b_decimal = int(binary, 2)
    t_decimal = int(ternary, 3)
    result = 0
    arr = [3**i for i in range(40)]
    for i in range(b_decimal, t_decimal + 1):
        chk = b_decimal ^ i
        if format(chk, 'b').count('1') == 1:
            chk2 = t_decimal - i
            if chk2 in arr:
                result = i
                break
    print(f'#{t} {result}')
