# BOJ_2628. 종이자르기

c, r = map(int, input().split())

n = int(input())

row_arr = [i for i in range(r)]
col_arr = [i for i in range(c)]
rows = []
cols = []
r_cnt = 0
c_cnt = 0
for _ in range(n):
    r_c, idx = map(int, input().split())
    if r_c == 0:
        rows.append(idx)
    else:
        cols.append(idx)
rows.sort()
cols.sort()
for r_idx in rows:
    row_arr.insert(r_cnt + r_idx, '#')
    r_cnt += 1
for c_idx in cols:
    col_arr.insert(c_cnt + c_idx, '#')
    c_cnt += 1

print(row_arr)
print(col_arr)

# print(' '.join(s for s in row_arr))


result = ''.join(str(s) for s in row_arr)
print(result)
