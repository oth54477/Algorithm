# num = '00000011001111'
# r = len(num) // 7
# result = ''
# cnt_0, cnt_1 = 0, 0
# for n in num:
#     if n == '1':
#         cnt_1 += 1
#         result += '0' * (cnt_0 // r)
#         cnt_0 = 0
#     else:
#         cnt_0 += 1
#         result += '1' * (cnt_1 // r)
#         cnt_1 = 0
# result += '0' * (cnt_0 // r) + '1' * (cnt_1 // r)
# print(result)

# n = 18
# arr = [input().strip().strip('0') for _ in range(n)]
# arr = set(arr)
# max_l = 0
# for i in arr:
#     l = len(i)
#     if l > max_l:
#         max_l = l
#         max_i = i


# for t in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     real_line = set()
#     for _ in range(1):
#         line = input().strip()
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
#     real_line -= {''}
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

# for t in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     real_line = set()
#     for _ in range(n):
#         line = input()[:m]
#         line = format(int(line, 16), 'b').strip('0')
#         if line:
#             real_line.add(line)
#     result = set()
#     for line in real_line:
#         cnt = 1
#         while True:
#             if line[-7*cnt :-1] in table:
#                 r = 7 * cnt
#                 break
#             else:
#                 cnt += 1
#         result.add(line[]

# arr = set([input()[:m].strip('0') for _ in range(n)])
# arr -= {''}
# result = set()
# for line in arr:
#     for line2 in arr:
#         if line in line2:
#             # arr -= {line2}
#             new_line = line2.replace(line, '').strip('0')
#             if new_line:
#                 result.add(new_line)
#             else:
#                 result.add(line)
# print(result)


def ratio_7(num):
    # print(num)
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


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    real_line = set()
    for _ in range(n):
        line = input()[:m]
        line = format(int(line, 16), 'b').strip('0')
        if line:
            real_line.add(line)
    result = set()
    print(real_line)
    for line in real_line:
        while line:
            print(line)
            cnt = 1
            while True:
                print(line[-7 * cnt :])
                if ratio_7(line[-7 * cnt :]) in table:
                    r = 7 * 8 * cnt
                    new_line = line[-r:]
                    if len(new_line) % 7 != 0:
                        new_line = ('0' * (7 - (len(new_line) % 7))) + new_line
                    result.add(new_line)
                    line = line[:-r].strip('0')
                    break
                else:
                    cnt += 1
    print(result)
