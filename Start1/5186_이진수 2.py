# 5186. 이진수 2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for t in range(1, int(input()) + 1):
    d = float(input())
    cnt = 1
    result = ''
    while d != 0.0:
        if cnt == 13:
            result = 'overflow'
            break
        a = 2 ** (-cnt)
        if d - a >= 0:
            d -= a
            result += '1'
        else:
            result += '0'
        cnt += 1
    print(f'#{t} {result}')
