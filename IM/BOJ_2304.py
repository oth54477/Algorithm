import sys

sys.stdin = open('input.txt')

# n = int(input())
# d = {}
# for _ in range(n):
#     idx, h = map(int, input().split())
#     d[idx] = h

# dic_sort = sorted(d.items())
# last_h = dic_sort[-1][0]
# arr = [0] * (last_h + 1)
# for i, v in sorted(d.items()):
#     arr[i] = v

# idx = 0
# max_height = max(arr)
# idx_reverse = False
# max_chk = arr.count(max_height) - 1

# while True:
#     if not idx_reverse:
#         if arr[idx + 1] == max_height:
#             idx_reverse = True
#             first_max = idx + 1
#             idx = last_h
#         elif arr[idx] >= arr[idx + 1]:
#             arr[idx + 1] = arr[idx]
#             idx += 1
#         elif arr[idx] < arr[idx + 1]:
#             idx += 1

#     else:
#         if arr[idx - 1] == max_height:
#             if max_chk:
#                 last_max = idx
#                 for i in range(first_max, last_max):
#                     arr[i] = max_height
#             break
#         elif arr[idx] >= arr[idx - 1]:
#             arr[idx - 1] = arr[idx]
#             idx -= 1
#         elif arr[idx] < arr[idx - 1]:
#             idx -= 1

# print(arr)
# print(sum(arr))


def chk(arr_s):
    for idx in range(len(arr_s) - 1):
        if arr_s[idx] >= arr_s[idx + 1]:
            arr_s[idx + 1] = arr_s[idx]
    return sum(arr_s)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
end_idx = max(list(zip(*arr))[0])

storage = [0] * (end_idx + 1)

for idx, h in arr:
    storage[idx] = h

max_h = max(storage)
max_idx = storage.index(max_h)
r_max_idx = end_idx - storage[::-1].index(max_h) + 1

arr1 = storage[:max_idx]
arr2 = storage[-1 : r_max_idx - 1 : -1]
print(max_h * (r_max_idx - max_idx) + chk(arr1) + chk(arr2))
