# while문 사용
def find_0(i, j):
    global row, col, cnt, number, snail, N
    while cnt < N - 1 and snail[row + i][col + j] == 0:
        number += 1
        row += i
        col += j
        snail[row][col] = number
        cnt += 1
    cnt = 0


# # 재귀함수
# def find_0(i, j):
#     global row, col, cnt, number, snail, N
#     if cnt >= N - 1 or snail[row + i][col + j] != 0:
#         cnt = 0
#         return None
#     number += 1
#     row += i
#     col += j
#     snail[row][col] = number
#     cnt += 1
#     find_0(i, j)


T = int(input())
for t in range(1, T + 1):

    # 다음에 입력할 곳의 값이 0이면 계속 0 이 아니면 스탑
    N = int(input())
    snail = [[0] * N for i in range(N)]  # 0으로 채워져 있는 2차원 배열 선언
    snail[0][0] = 1  # 0,0에 1 할당
    number = 1  # 할당해줄 숫자
    row, col, cnt = 0, 0, 0
    while number != N**2:  # number가 N의 제곱이 될 때까지 반복
        find_0(0, 1)  # 오른쪽 탐색, 채우기
        find_0(1, 0)  # 아래쪽 탐색, 채우기
        find_0(0, -1)  # 왼쪽 탐색, 채우기
        find_0(-1, 0)  # 위쪽 탐색, 채우기
    print(f'#{t}')
    for rows in snail:
        for cols in rows:
            print(cols, end=' ')
        print()
