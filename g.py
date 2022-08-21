def paint(idx, line):
    if idx % 2 == 0:
        cnt1 = format(int(('0b' + line), 2) ^ 170, 'b').count('1')
        cnt2 = format(int(('0b' + line), 2) ^ 85, 'b').count('1')
    else:
        cnt1 = format(int(('0b' + line), 2) ^ 85, 'b').count('1')
        cnt2 = format(int(('0b' + line), 2) ^ 170, 'b').count('1')
    return cnt1, cnt2


n, m = map(int, input().split())
board = [input().replace('W', '1').replace('B', '0') for _ in range(n)]
min_num1 = n * m
min_num2 = n * m
for k in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        cnt1, cnt2 = 0, 0
        for i in range(8):
            num1, num2 = paint(i, board[k + i][j : j + 8])
            cnt1 += num1
            cnt2 += num2
        if min_num1 >= cnt1:
            min_num1 = cnt1
        if min_num2 >= cnt2:
            min_num2 = cnt2

print(min(min_num1, min_num2))
