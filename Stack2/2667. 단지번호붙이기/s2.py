def dfs(row, col):
    global cnt
    cnt += 1
    visited[row][col] = True

    for dr in d:
        # 델타 이동
        next_row, next_col = row + dr[0], col + dr[1]
        # 다음 이동 장소가 범위를 벗어나지 않고, 방문 x, 값이 1 인
        if (
            (0 <= next_row < n)
            and (0 <= next_col < n)
            and (not visited[next_row][next_col])
            and (apt_info[next_row][next_col] == 1)
        ):
            dfs(next_row, next_col)


n = int(input())

apt_info = [list(map(int, input())) for _ in range(n)]

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[False] * n for _ in range(n)]
cnt_arr = []
for r in range(n):
    for c in range(n):
        if (apt_info[r][c] == 1) and (not visited[r][c]):
            cnt = 0
            dfs(r, c)
            cnt_arr.append(cnt)


cnt_arr.sort()
print(len(cnt_arr), *cnt_arr, sep='\n')
