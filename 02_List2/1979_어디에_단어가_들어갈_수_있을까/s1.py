T = input()
for t in range(1, int(T) + 1):
    N, K = map(int, input().split())
    rows, cols = N, N
    count = 0
    arr = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(0, N):
        A = input()
        B = list(map(int, A.split()))
        C = A.replace(" ", "").split("0")
        for f_k in range(0, len(C)):
            if len(C[f_k]) == K:
                count += 1
        for j in range(0, N):
            arr[i][j] = B[j]
    for row in range(0, N):
        col_find = ""
        for col in range(0, N):
            col_find += str(arr[col][row])
            D = col_find.replace(" ", "").split("0")
        for f_k in range(0, len(D)):
            if len(D[f_k]) == K:
                count += 1
    print(f'#{t} {count}')
