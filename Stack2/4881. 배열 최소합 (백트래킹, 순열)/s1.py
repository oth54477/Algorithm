import sys

sys.stdin = open('sample_input.txt')


def min_sum(sum_arr, depth):
    global ms
    # depth가 n이 되면
    if depth == n:
        # ms와 합 비교
        if ms > sum(sum_arr):
            # 더 작은 값 저장
            ms = sum(sum_arr)
        return
    # 이미 ms보다 합이 커지만 return
    if sum(sum_arr) >= ms:
        return
    for i in range(n):
        if not visited[i]:
            sum_arr.append(arr[depth][i])
            visited[i] = True
            min_sum(sum_arr, depth + 1)
            sum_arr.pop()
            visited[i] = False


for t in range(1, int(input()) + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    sum_arr = []
    ms = 27
    min_sum(sum_arr, 0)
    print(f'#{t} {ms}')
