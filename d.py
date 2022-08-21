# max_result = 0
# for i in range(9):
#     num = list(map(int, input().split()))
#     max_n = max(num)
#     max_idx = (i + 1, num.index(max_n) + 1)

#     if max_result < max_n:
#         max_result = max_n
#         result_idx = max_idx

# print(f'{max_result}\n{result_idx[0]} {result_idx[1]}')


arr = [list(map(int, input().split())) for _ in range(9)]
max_num = 0

for row in range(9):
    for col in range(9):
        num = arr[row][col]
        if max_num <= num:
            max_num = num
            max_idx = f'{row+1} {col+1}'
print(f'{max_num}\n{max_idx}')
