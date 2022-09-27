# 4615. 재미있는 오셀로 게임
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE&problemTitle=%EC%98%A4%EC%85%80%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&

import sys

sys.stdin = open('sample_input(1).txt')

def othello(row, col, color):
    for d in range(8):                                                      # 8방향 이동
        nr, nc = row + dx[d], col + dy[d]                                   # 이동할 nr, nc
        if 0 <= nr < n and 0 <= nc < n and field[nr][nc] == colors[color]:  # 범위안에 있고, 놓은 돌 색과 다를 때
            find_color(nr, nc, color, d)                                    # 감싸져 있는지 찾기


def find_color(row, col, color, d):
    global find_status
    find_status = False                                                     # 한 방향에서 같은 색 돌을 찾았는지?
    if 0 <= row < n and 0 <= col < n and field[row][col]:                   # 범위를 벗어나지 않고, 돌이 있는 경우
        if field[row][col] == color:                                        # 같은 색 돌을 찾으면
            find_status = True                                              # 상태 = True
            return                                                          # return
        elif field[row][col] == colors[color]:                              # 다른 색 돌이면?
            find_color(row + dx[d], col + dy[d], color, d)                  # 재귀!
        if find_status:                                                     # find상태가 True이면
            field[row][col] = colors[field[row][col]]                       # 색 바꿔주기
    else:                                                                   # 범위 벗어나면
        return                                                              # return
    
colors = {1:2, 2:1}                             # 돌을 바꾸기 위한 딕셔너리
table = {4:[(1,1),(1,2),(2,2),(2,1)], 6:[(2,2),(2,3),(3,3),(3,2)], 8:[(3,3),(3,4),(4,4),(4,3)]} # 초기 위치를 위한 딕셔너리
dx = [-1, 1, 0, 0, -1, -1, 1, 1]        # 델타이동 
dy = [0, 0, -1, 1, -1, 1, -1, 1]        # 델타이동
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    field = [[0] * n for _ in range(n)]
    cnt = 0
    find_status = False
    for r, c in table[n]:               # 초기 위치 설정 딕셔너리에서 값을 받아서 r, c에 할당
        if cnt % 2 == 0:                    
            field[r][c] = 2
        else:
            field[r][c] = 1
        cnt += 1
    for _ in range(m):
        row, col, color = map(int, input().split())
        row -= 1                        # 리스트는 0 부터 시작하기 때문에 1 빼준다
        col -= 1                        # 리스트는 0 부터 시작하기 때문에 1 빼준다
        field[row][col] = color         # 주어진 위치에 돌 놓기
        othello(row,col,color)          # 함수 실행
    white, black = 0,0                  # 백돌 흑돌 개수 초기값 설정
    for line in field:                  # 판에서 한 줄씩 받아오기
        black += line.count(1)          # 1의 개수를 흑돌에 더하기    
        white += line.count(2)          # 2의 개수를 백돌에 더하기
    print(f'#{t} {black} {white}')
        