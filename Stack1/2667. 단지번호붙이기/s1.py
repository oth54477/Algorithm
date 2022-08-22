def dfs(row, col):
    global d, cnt, c
    visited[row][col] = True

    for dr in d:
        next_row, next_col = row + dr[0], col + dr[1]
        if (
            (0 <= next_row < n)
            and (0 <= next_col < n)
            and (not visited[next_row][next_col])
        ):
            if apt_info[next_row][next_col] > 0:
                cnt_arr[cnt] += 1
                dfs(next_row, next_col)
            else:
                print(cnt_arr)
                print(cnt)
                if cnt_arr[cnt] != 0:
                    cnt += 1
                dfs(next_row, next_col)

    # for next_v in graph[v]:
    #     if not visited[next_v]:
    #         dfs(next_v)


n = int(input())

apt_info = [list(map(int, input())) for _ in range(n)]

# d_row = [-1, 1, 0, 0]  # 상 하 좌 우
# d_col = [0, 0, -1, 1]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[False] * n for _ in range(n)]
cnt_arr = [0] * 4
cnt, c = 1, 0
dfs(0, 0)
print(cnt_arr)
