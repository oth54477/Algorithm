def success_rate(memo):
    for i in range(1, n):
        for j in range(n):
            tmp = set()
            value = rate[i][j]
            for r in memo[j]:
                tmp.add(r * value)
            memo[j] = tmp
    return memo
                
            
    


for t in range(1, int(input()) + 1):
    n = int(input())
    rate = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]
    visited = [False] * n
    start_arr = []
    for i in range(n):
        arr = rate[0][:]
        arr.pop(i)
        start_arr.append(set(arr) - {0.0})
    print(start_arr)
    result = success_rate(start_arr)
    print(result)
    # max_rate = round(max(result) * 100, 6)  
    # print(f'#{t} {max_rate:.6f}')