n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# cnt = 0
pop_arr = []
arr.sort()
new_arr = sorted(arr)
for i in range(1, n - 1):
    if arr[i][1] <= arr[i + 1][1] and arr[i][1] <= arr[i - 1][1]:
        pop_arr.append(i)

print(pop_arr)


# 모르겠다.
