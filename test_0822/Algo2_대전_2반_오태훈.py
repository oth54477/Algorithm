for t in range(1, int(input())+1):
    n = int(input())
    # N x N 2차원 배열 입력
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 3 x 3 패턴
    arr_filter = [list(map(int, input().split())) for _ in range(3)]
    # 9개 값이 모두 일치하는 개수 카운트
    total_cnt = 0
    # (n-3+1) * (n-3+1)개의 경우의 수 가능
    for j in range(n - 3 + 1):
        for i in range(n - 3 + 1):
            # row마다 일치하는지 확인하기 위한 cnt 초기화
            cnt = 0
            for row in range(3):
                # 슬라이싱을 사용하지 않기 위해 col 에 0,1,2 할당
                for col in range(3):
                    check_arr = arr[i + row][j + col]
                    # 값이 일치하면 cnt에 +1
                    if check_arr == arr_filter[row][col]:
                        cnt += 1
            # cnt가 9이상이면 9개 값이 모두 일치
            if cnt >= 9:
                # total_cnt에 +1
                total_cnt += 1
    print(f'#{t} {total_cnt}')
