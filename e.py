cnt_arr = []
for i in range(4):
    line = list(map(str, input()))
    cnt_arr += line[::2]
    line = list(map(str, input()))
    cnt_arr += line[1::2]
print(cnt_arr.count('F'))
