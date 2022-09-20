# 1242. 암호코드스캔
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD&categoryId=AV15JEKKAM8CFAYD&categoryType=CODE&problemTitle=1242&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

table = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

r = {}


def ratio_7(num):
    r = len(num) // 7
    result = ''
    cnt_0, cnt_1 = 0, 0
    for n in num:
        if n == '1':
            cnt_1 += 1
            result += '0' * (cnt_0 // r)
            cnt_0 = 0
        else:
            cnt_0 += 1
            result += '1' * (cnt_1 // r)
            cnt_1 = 0
    result += '0' * (cnt_0 // r) + '1' * (cnt_1 // r)
    return result


def chk(line):
    cnt, chk, result = 0, 0, 0
    l = len(line)
    ll = l // 8
    for i in range(0, l, ll):
        cnt += 1
        bin_str = line[i : i + ll]
        print(t, bin_str)
        if len(bin_str) > 7:
            bin_str = ratio_7(bin_str)
        num = table[bin_str]
        if cnt % 2 == 0:
            chk += num
        else:
            chk += num * 3
        result += num
    if chk % 10 != 0:
        result = 0
    return result


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    real_line = set()
    for _ in range(n):
        line = input()[:m]
        if not line.isnumeric():
            arr = line.split('0')
            cnt = 0
            result = ''
            for i in arr:
                if i:
                    result += i
                else:
                    cnt += 1
                if cnt > 1:
                    real_line.add(result)
                    result = ''
                    cnt = 0
    real_line.add(result)
    real_line -= {''}
    print(real_line)
    for line in list(real_line):
        line = format(int(line, 16), 'b').rstrip('0')
        line = ('0' * (7 - (len(line) % 7))) + line

    result = chk(line)
    r[t] = result
    print(f'#{t} {result}')
    print(r)
