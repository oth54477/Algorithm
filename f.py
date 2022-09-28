# 5188. 최소 합
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# dfs를 이용한 풀이

def dfs(row, col):
    global sum_num, result
    visited[row][col] = True                                    # 방문처리
    if result <= sum_num:                                       # 지금까지 지나온 숫자의 합이 result 보다 커지만 return
        return
    for d in range(2):                                          # 아래, 오른쪽 방향으로만 이
        nr, nc = row + dx[d], col + dy[d]                       # 이동할 위치
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]: # 이동할 수 있는지 확인
            sum_num += arr[nr][nc]                              # sum_num에 숫자 더해주기
            dfs(nr, nc)                                         # 이동 위치로 재귀
            visited[nr][nc] = False                             # 방문 처리 해제
            if nr == (n - 1) and nc == (n - 1):                 # 오른쪽 맨 아래에 도착했을 때
                if result > sum_num:                            # result보다 sum_num이 작으면
                    result = sum_num                            # result에 값 저장
            sum_num -= arr[nr][nc]                              # 더해준 값 다시 빼주기


dx = [1, 0]                                                     # 아래, 오른쪽
dy = [0, 1]                                                     # 아래, 오른쪽
for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = 10 * n * n                                         # 나올 수 있는 최댓값 설정
    sum_num = arr[0][0]                                         # 초기 위치 값 저장
    dfs(0, 0)                                                   # 시작 위치에서 dfs 시작
    print(f'#{t} {result}')
