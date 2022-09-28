# # 5188. 최소 합
# # https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# # dfs를 이용한 풀이

# def dfs(row, col):
#     global sum_num, result
#     visited[row][col] = True                                    # 방문처리
#     if result <= sum_num:                                       # 지금까지 지나온 숫자의 합이 result 보다 커지만 return
#         return
#     for d in range(2):                                          # 아래, 오른쪽 방향으로만 이
#         nr, nc = row + dx[d], col + dy[d]                       # 이동할 위치
#         if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]: # 이동할 수 있는지 확인
#             sum_num += arr[nr][nc]                              # sum_num에 숫자 더해주기
#             dfs(nr, nc)                                         # 이동 위치로 재귀
#             visited[nr][nc] = False                             # 방문 처리 해제
#             if nr == (n - 1) and nc == (n - 1):                 # 오른쪽 맨 아래에 도착했을 때
#                 if result > sum_num:                            # result보다 sum_num이 작으면
#                     result = sum_num                            # result에 값 저장
#             sum_num -= arr[nr][nc]                              # 더해준 값 다시 빼주기


# dx = [1, 0]                                                     # 아래, 오른쪽
# dy = [0, 1]                                                     # 아래, 오른쪽
# for t in range(1, int(input()) + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[False] * n for _ in range(n)]
#     result = 10 * n * n                                         # 나올 수 있는 최댓값 설정
#     sum_num = arr[0][0]                                         # 초기 위치 값 저장
#     dfs(0, 0)                                                   # 시작 위치에서 dfs 시작
#     print(f'#{t} {result}')


# import sys

# sys.stdin = open('sample_input.txt')

# 2차원 리스트 내에 중복된 리스트 제거 함수
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


# 순열 생성 함수
def permutations(depth):
    global answer
    if depth == l:
        temp = []
        for i in range(l):
            temp.append(numbers[i])
        temp = tuple(temp)
        answer.add(temp)
        return
    for i in range(depth, l):
        numbers[depth], numbers[i] = numbers[i], numbers[depth]
        permutations(depth + 1)
        numbers[depth], numbers[i] = numbers[i], numbers[depth]


T = int(input())

# 우 하

dx = [0, 1]
dy = [1, 0]

for test_case in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 순열
    answer = set()
    numbers = []
    for i in range(N - 1):
        numbers.append(0)
        numbers.append(1)
    l = len(numbers)
    permutations(0)
    # 중복된 순열 제거
    answer = list(answer)
    answer = get_unique_list(answer)

    temp = 0

    # sums 에 최대값 저장
    for i in range(N):
        for j in range(N):
            temp += arr[i][j]

    sums = []
    sums.append(temp)
    path_sum = arr[0][0]
    position_x = 0
    position_y = 0

    # 순열을 나타내는 2차원 리스트에 접근
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            position_x += dx[answer[i][j]]
            position_y += dy[answer[i][j]]
            path_sum += arr[position_x][position_y]
            if path_sum >= min(sums):
                break
        sums.append(path_sum)
        position_x = 0
        position_y = 0
        path_sum = arr[0][0]
    print(f'#{test_case} {min(sums)}')
