# 1949. 등산로 조성
'''
1
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
'''


def dfs(row, col):
    global cnt_arr, max_r
    visited[row][col] = True
    for dr in d:
        nr, nc = row + dr[0], col + dr[1]

        if (
            0 <= nr < n
            and 0 <= nc < n
            and not visited[nr][nc]
            and m_map[nr][nc] < m_map[row][col]
        ):
            cnt_arr.append(m_map[nr][nc])
            dfs(nr, nc)
        elif len(cnt_arr) > len(max_r):
            max_r = cnt_arr
        cnt_arr = []


d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    cnt = 0
    cnt_arr = []
    max_r = []
    m_map = [list(map(int, input().split())) for _ in range(n)]
    total_max = max(list(map(lambda x: max(x), m_map)))
    for row in range(n):
        for col in range(n):
            if m_map[row][col] == total_max:
                visited = [[False] * n for _ in range(n)]
                dfs(row, col)
    print(max_r)
