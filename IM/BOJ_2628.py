# BOJ_2628. 종이자르기

c, r = map(int, input().split())

n = int(input())

row_arr = [i for i in range(r)]
col_arr = [i for i in range(c)]
# rows, cols, r_cnt, c_cnt = [], [], 0, 0
rows, cols, r_cnt, c_cnt = [0], [0], 0, 0
for _ in range(n):
    cut, idx = map(int, input().split())
    if cut == 0:
        rows.append(idx)
    else:
        cols.append(idx)

rows.sort()
cols.sort()

rows.append(r)
cols.append(c)
max_r, max_c = 0, 0
for rr in range(1, len(rows)):
    rrr = rows[rr] - rows[rr - 1]
    if max_r < rrr:
        max_r = rrr
for cc in range(1, len(cols)):
    ccc = cols[cc] - cols[cc - 1]
    if max_c < ccc:
        max_c = ccc
print(max_c * max_r)


# rows.sort()
# cols.sort()
# for r_idx in rows:
#     row_arr.insert(r_cnt + r_idx, '#')
#     r_cnt += 1
# for c_idx in cols:
#     col_arr.insert(c_cnt + c_idx, '#')
#     c_cnt += 1


# row_arr = ''.join(str(s) for s in row_arr).split('#')
# col_arr = ''.join(str(s) for s in col_arr).split('#')


# print(
#     max(list(map(len, row_arr)))
#     * max(list(map(len, col_arr)))
# )
