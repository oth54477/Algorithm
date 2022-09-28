# 1242. 암호코드스캔
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD&categoryId=AV15JEKKAM8CFAYD&categoryType=CODE&problemTitle=1242&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

# table = {
#     '0001101': 0,
#     '0011001': 1,
#     '0010011': 2,
#     '0111101': 3,
#     '0100011': 4,
#     '0110001': 5,
#     '0101111': 6,
#     '0111011': 7,
#     '0110111': 8,
#     '0001011': 9,
# }

# r = {}


# def ratio_7(num):
#     r = len(num) // 7
#     result = ''
#     cnt_0, cnt_1 = 0, 0
#     for n in num:
#         if n == '1':
#             cnt_1 += 1
#             result += '0' * (cnt_0 // r)
#             cnt_0 = 0
#         else:
#             cnt_0 += 1
#             result += '1' * (cnt_1 // r)
#             cnt_1 = 0
#     result += '0' * (cnt_0 // r) + '1' * (cnt_1 // r)
#     return result


# def chk(line):
#     cnt, chk, result = 0, 0, 0
#     l = len(line)
#     ll = l // 8
#     for i in range(0, l, ll):
#         cnt += 1
#         bin_str = line[i : i + ll]
#         print(t, bin_str)
#         if len(bin_str) > 7:
#             bin_str = ratio_7(bin_str)
#         num = table[bin_str]
#         if cnt % 2 == 0:
#             chk += num
#         else:
#             chk += num * 3
#         result += num
#     if chk % 10 != 0:
#         result = 0
#     return result


# for t in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     real_line = set()
#     for _ in range(n):
#         line = input()[:m]
#         if not line.isnumeric():
#             arr = line.split('0')
#             cnt = 0
#             result = ''
#             for i in arr:
#                 if i:
#                     result += i
#                 else:
#                     cnt += 1
#                 if cnt > 1:
#                     real_line.add(result)
#                     result = ''
#                     cnt = 0
#     real_line.add(result)
#     real_line -= {''}
#     print(real_line)
#     for line in list(real_line):
#         line = format(int(line, 16), 'b').rstrip('0')
#         line = ('0' * (7 - (len(line) % 7))) + line

#     result = chk(line)
#     r[t] = result
#     print(f'#{t} {result}')
#     print(r)


'''
1. 암호코드의 흰색, 파란색의 넓이 비(ratio)와 숫자 값을 딕셔너리로 매핑한다.
2. 비(ratio)가 3:1:1:2 라고 하면 사실 이를 판별하는 건 뒤에 세 자리(1:1:2)만 있어도 가능하다.
3. 따라서 암호코드를 "왼쪽->오른쪽"이 아니라 "오른쪽->왼쪽" 방향으로 읽는 것이 편하다.
4. 먼저 배열에 있는 모든 16진수 숫자 하나 당, 길이가 4인 2진수로 변환한다. (ex. 4 -> 0100, F -> 1111)
5. 그러면 16진수 배열은 2진수 배열이 된다. 이제 각 줄 마다 오른쪽에서 부터 읽어간다.
6. 오른쪽에서 부터 읽는 경우, 처음에는 1의 구간을, 그 다음에는 0의 구간, 그 다음에는 다시 1 구간, 그 다음에는 0의 구간이 반복되는 규칙을 이용한다.
7. 마지막 0의 구간은 사용하지 않는 비(ratio)이므로 1을 만날 때 까지 계속 지나쳐간다. 1을 만났다는 것은 다른 새로운 암호코드가 있다는 것이다.
8. 그래서 각 1과 0의 개수를 세고, 비(ratio)를 계산한다. 이 때 1:1:2가 아니라 길이가 2배라서 2:2:4 인 경우가 있을 수도 있으니, (2, 2 ,4) 중 가장 작은 2로 모두 나누면 (1, 1, 2)를 만들 수 있다.
9. 아까 만들었던 딕셔너리를 통해 조회하면 해당 암호코드에 해당하는 10진수가 나온다.
10. 이러한 10진수가 8개가 될 때까지 반복하고, 8개가 되면 `(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드` 식을 이용하여 10의 배수라면 결과값에 합을 더한다.
11. 배열의 한 줄에 2개 이상의 암호코드가 있을 수 있으므로, 10진수 8개가 나왔더라도 다른 새로운 암호코드가 없을 때 까지 계속 왼쪽으로 이동한다.
12. 모든 배열을 탐색하고 결과 값을 출력한다.
13. (주의) 동일 암호 코드의 중복 계산을 방지해야 한다.
'''


import sys

sys.stdin = open('sample_input.txt')


table = {
    "211": "0",
    "221": "1",
    "122": "2",
    "411": "3",
    "132": "4",
    "231": "5",
    "114": "6",
    "312": "7",
    "213": "8",
    "112": "9",
}


def find_ratio():                   # 비율을 찾는 함수 ratio리스트를 반환한다.
    global binary
    i_0 = binary.index('0')         # index함수를 이용해 문자열에서 0을찾는다.
    binary = binary[i_0:]           # 앞의 0들을 지운다.
    i_1 = binary.index('1')         # index함수를 이용해 문자열에서 1을찾는다.
    binary = binary[i_1:]           # 앞의 1들을 지운다.
    if '0' in binary:               # 0이 문자열에 있는 경우
        i_00 = binary.index('0')    # index함수를 이용해 문자열에서 0을찾는다.
    else:                           # 없는 경우
        i_00 = len(binary)          # 전체 길이를 찾는다.
    ratio = [i_0, i_1, i_00]        # 비율을 리스트로 저장한다.
    binary = binary[i_00:]          # 지운다.
    return ratio


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    lines = set()                               # 중복을 제거하기 위해 set()을 사용한다.
    for _ in range(n):
        line = input()[:m].strip()
        if not line.isnumeric():                # 숫자가 아닌 문자열이 포함되어 있으면
            lines.add(line.strip('0'))          # 양족의 0을 지우고 set에 더해준다.

    codes = set()
    for line in lines:
        binary = format(int(line, 16), 'b')                     # 2진수로 변환
        binary = binary.strip('0')                              # 양쪽의 0을 지움
        code = ''
        while binary:                                           # binary 문자열이 빈 문자열이 아닌동안 반복
            ratio = find_ratio()                                # find_ratio() 함수를 사용해 비율을 찾는다.
            min_num = min(ratio)                                # 비율에서 가장 작은 값
            a, b, c = map(lambda x: str(x//min_num), ratio)     # 가장 작은 값으로 모두 나눠 정확한 비율을 구한다.
            ratio = a+b+c                                       # 문자열로 합친다.
            code += table[ratio]                                # table에서 숫자를 찾는다.
            binary = binary.strip('0')                          # 맨 앞의 0을 지운다.
            if len(code) == 8:                                  # 한 암호를 다 찾았을 때 (8자리)
                codes.add(code)                                 # codes에 저장
                code = ''                                       # code를 빈 문자열로 초기화
    result = 0
    for code in codes:
        chk_num, sum_num = 0, 0
        for idx, num in enumerate(code):                        # 암호 검증
            num = int(num)
            if idx % 2 == 0:                                    # 홀수일 때
                chk_num += num * 3                              # 곱하기 3을 하고 더한다.
            else:                                               # 짝수일 때
                chk_num += num                                  # 그냥 더한다.
            sum_num += num                                      # 전부 더한 값을 구한다.
        if chk_num % 10 == 0:                                   # 검증하기 위한 숫자가 10의 배수이면
            result += sum_num                                   # result에 전부 더한 값을 더한다.

    print(f'#{t} {result}')
