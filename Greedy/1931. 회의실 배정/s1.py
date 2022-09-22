# 1931. 회의실 배정
# https://www.notion.so/hphk-edu/Algorithm-e424c5461c58482ca6cf4a1080f1f880
import sys

input = sys.stdin.readline
n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x: (x[1], x[0]))
i, j, cnt = 0, 1, 1
while j < n:
    if times[i][1] <= times[j][0]:
        cnt += 1
        i = j
        j += 1
    else:
        j += 1
print(cnt)