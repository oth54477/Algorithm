# def paint(arr):
#     cnt = 0
#     for idx, line in enumerate(arr):
#         if idx % 2 == 0:
#             line = line.replace('WB', '')
#             cnt += len(line)
#         if idx % 2 != 0:
#             line = line.replace('BW', '')
#             cnt += len(line)
#     return cnt // 2


# n, m = map(int, input().split())
# arr = [input() for _ in range(n)]
# min_num = n * m
# for i in range(n - 8 + 1):
#     for j in range(m - 8 + 1):
#         num = paint(arr[i : i + 8][j : j + 8])
#         if min_num >= num:
#             min_num = num


# print(min_num)


def paint(arr):
    cnt = 0
    for idx, line in enumerate(arr):
        if idx % 2 == 0:
            cnt += format(int(('0b' + line), 2) ^ 170, 'b').count('1')
        if idx % 2 != 0:
            cnt += format(int(('0b' + line), 2) ^ 85, 'b').count('1')

    return cnt


n, m = map(int, input().split())
arr = [input().replace('W', '1').replace('B', '0') for _ in range(n)]
min_num = n * m
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        num = paint(arr[i : i + 8][j : j + 8])
        if min_num >= num:
            min_num = num


print(min_num)
