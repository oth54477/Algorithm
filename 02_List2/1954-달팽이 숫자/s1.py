from tracemalloc import Snapshot
from winsound import SND_FILENAME


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    snail = [[0]*n for i in range(n)]
    go_row = [0, -1, 0, 1] # 하, 좌, 상, 우
    go_col = [1, 0, -1, 0]

    row = 0
    col = 0
    count = 0
    for m in range(n-1, 0, -1):
        if count == 0:
            for _ in range(m):
                snail[row + go_row[0]][col + go_col[0]] = 
            for _ in range(m):
                snail[row + go_row[1]][col + go_col[1]]
            count = 1
        else:
            for _ in range(m):
                snail[row + go_row[2]][col + go_col[2]]
            for _ in range(m):
                snail[row + go_row[3]][col + go_col[3]]
            count = 0

            
        

