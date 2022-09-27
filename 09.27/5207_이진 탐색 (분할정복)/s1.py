def binary_search(arr, left, right, num):           # 이진 탐색
    global cnt, s           
    if arr:                                         # 리스트에 값이 있을 때
        middle = (left + right) // 2                # 중간 위치 구하기
        middle_num = arr[middle]                    # 중간 위치의 값 구하기
        if num > middle_num:                        # 탐색 값이 더 클때
            if s == 1:                              # 같은방향 연속 2번이면 return
                return
            s = 1
            binary_search(arr, middle+1, right, num) # 오른쪽 반절로 재귀
        elif num < middle_num:                      # 작을 때
            if s == 0:
                return
            s = 0
            binary_search(arr, left, middle - 1, num) # 왼쪽 반절로 재귀
        else:
            cnt += 1                                    # 찾으면 +1
    return

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    nums_a = sorted(list(map(int, input().split())))
    nums_b = list(map(int, input().split()))
    cnt = 0                                             # 조건에 맞는 숫자의 개수
    for num in nums_b:                                  # B에서 숫자 하나씩 할당
        s = -1                                          # 방향 상태 초기값 -1
        binary_search(nums_a, 0, n-1,num)               # 이진 탐색 시작
    print(f'#{t} {cnt}')
        
    