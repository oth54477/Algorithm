# BOJ_2477. 첨외밭

k = int(input())


ds = []
vs = []
for _ in range(6):
    d, v = map(int, input().split())
    ds.append(d)
    vs.append(v)

max_idx = vs.index(max(vs))

ds = ds[max_idx:] + ds[:max_idx]
vs = vs[max_idx:] + vs[:max_idx]

cnt = [0] * 5
for idx, value in enumerate(ds):
    cnt[value] += 1
    if cnt[value] >= 2:
        start_idx = idx

m = {0, 1, 2, 3, 4, 5} - {0, start_idx, start_idx - 1, start_idx - 2, start_idx - 3}
print((vs[0] * vs[list(m)[0]] - vs[start_idx - 1] * vs[start_idx - 2]) * k)
