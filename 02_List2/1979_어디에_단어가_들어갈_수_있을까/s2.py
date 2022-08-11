for t in range(1, int(input())):
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    
    for row in range(n):
        window_sum = arr[row][0] + arr[row][1] + arr[row][2]
        for col in range(1, n-k):
            for i in range(k):
                window_sum += arr[row][col+i]
                
