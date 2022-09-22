import sys
sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    # arr = [list(map(int, input().split())) for _ in range(n)]
    arr = []
    for _ in range(n):
        s, e = map(int, input().split())
    arr.sort(key=lambda x: (x[1], x[0]))


    # print(arr)
    time = [0] * 26
    cnt = 0
    for i in arr:
        if sum(time[i[0]:i[1]+1]) == time[i[0]] + time[i[1]]:
            # print(i)
            for j in range(i[0], i[1] + 1):
                time[j] = 1
            cnt += 1
    # print(time) 
    print(f'#{t} {cnt}')



import sys
from itertools import permutations

for t in range(1, int(input()) + 1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]

    time.sort(key=lambda x: x[1])

    i, j, cnt = 0,1,1

    while j < n:
        if time[i][1] <= time[j][0]:
            cnt += 1
            i = j
            j += 1
        else:
            j += 1
    print(f'#{t} {cnt}')