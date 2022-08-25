import sys

sys.stdin = open('sample_input.txt')


def find_min(depth):
    global min_sum, sum_num
    # 이미 min_sum보다 합이 커지만 return
    if sum_num >= min_sum:
        return
    # depth가 n이 되면
    if depth == n:
        # min_sum와 합 비교
        if min_sum > sum_num:
            # 더 작은 값 저장
            min_sum = sum_num
        return
    for i in range(n):
        if not visited[i]:
            sum_num += arr[depth][i]
            visited[i] = True
            find_min(depth + 1)
            sum_num -= arr[depth][i]
            visited[i] = False


for t in range(1, int(input()) + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    # min_sum에 나올 수 있는 최대값인 9*n 저장
    min_sum, sum_num = 9 * n, 0
    # 재귀 시작
    find_min(0)
    print(f'#{t} {min_sum}')
