# 2105. 디저트 카페 (모의 A형)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE&problemTitle=2105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

def dfs(row, col, d, cnt):
    global max_cnt
    d %= 4
    while True:
        nr, nc = row + dx[d], col + dy[d]
        if start[0] == nr and start[1] == nc:
            max_cnt = max(max_cnt, cnt+1)
            return
        if sum(d_visited) == 4:
            return
        if 0 <= nr < n and 0 <= nc < n and not visited[arr[nr][nc]]:
            d_visited[d] = 1
            visited[arr[nr][nc]] = True
            dfs(nr, nc, d+1, cnt + 1)
            visited[arr[nr][nc]] = False
            d_visited[d] = 0
        else:
            break




dx = [1, -1, -1, 1] # 오른쪽아래, 오른쪽위, 왼쪽위, 왼쪽 아래
dy = [1, 1, -1, -1]
for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d_visited = [0] * 4
    visited = [False] * 101
    max_cnt = -1
    for row in range(n):
        for col in range(n):
            start = [row, col]
            visited[arr[row][col]] = True
            dfs(row, col, 0, 0)
            visited[arr[row][col]] = False
    print(f'#{t} {max_cnt}')





# # 2105. 디저트 카페 (모의 A형)
# # https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE&problemTitle=2105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
#

# 대각선 방향
# directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
#
#
# def dfs(i, j, direction_type, dessert_cnt):
#     global ans
#
#     # 직진 or 꺾기
#     if direction_type < 3:                     # 방향 이동
#         tmp = direction_type + 2
#     else:
#         tmp = direction_type + 1
#
#     for k in range(direction_type, tmp):
#         ni = i + directions[k][0]
#         nj = j + directions[k][1]
#
#         if start[0] == ni and start[1] == nj:   # 왔던 곳으로 돌아옴
#             ans = max(ans, dessert_cnt)
#             return
#
#         # 범위 벗어나면 X
#         if 0 <= ni < N and 0 <= nj < N:
#             if dessert_visited[arr[ni][nj]] == False:  # 방문하지 않은 카페 & 먹지 않은 디저트
#
#                 dessert_visited[arr[ni][nj]] = True
#
#                 dfs(ni, nj, k, dessert_cnt + 1)
#
#                 dessert_visited[arr[ni][nj]] = False
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(list(map(int, input().split())) for _ in range(N))
#
#     dessert_visited = [False] * 101 # 방문 처리
#     ans = -1    # 결과
#
#     # 사각형 모양을 그리며 출발하고 카페로 돌아와야 함.
#
#     for i in range(N):
#         for j in range(N):
#             start = (i, j)  # 시작 위치
#             dessert_visited[arr[i][j]] = True       # 시작 위치 방문 표시
#
#             dfs(i, j, 0, 1)                         # dfs
#
#             dessert_visited[arr[i][j]] = False      # 시작 위치 방문 제거
#
#     print(f'#{tc} {ans}')
