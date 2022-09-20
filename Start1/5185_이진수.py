# 5185. 이진수
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for t in range(1, int(input()) + 1):
    n, hex_s = map(str, input().split())
    result = ''
    for h in hex_s:
        bin_s = format(int(h, 16), 'b')
        bin_s = ('0' * (4 - len(bin_s))) + bin_s
        result += bin_s
    print(f'#{t} {result}')
