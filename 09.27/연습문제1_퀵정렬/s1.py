def partition(arr, left, right):
    pivot = arr[left]                           # 맨 왼족을 피벗 설정
    i, j = left, right                          # i, j 설정
    while i <= j:                               # j가 i보다 더 큰 동안 반복
        while i <= j and arr[i] <= pivot:       # i위치의 값이 pivot보다 클때까지 반복
            i += 1                              # i 오른쪽으로 움직이며 탐색
        while i <= j and arr[j] >= pivot:       # j위치의 값이 pivot보다 작을때까지 반복
            j -= 1                              # j 왼족으로 움직이며 탐색
        if i < j:                               # i와 j의 위치가 반전되면
            arr[i], arr[j] = arr[j], arr[i]     # 서로 값 바꾸기
    arr[left], arr[j] = arr[j], arr[left]       # 피벗을 가운데로 보내기
    return j

def quick_sort(arr, left, right):
    if left < right:                            # 오른쪽이 더 크다면
        middle = partition(arr, left, right)    # 분할을 위해 중간 값 위치 찾기
        quick_sort(arr, left, middle - 1)       # 왼족 재귀
        quick_sort(arr, middle + 1, right)      # 오른쪽 재귀

for t in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers) - 1)    # 퀵 정렬 (리스트, 왼족 끝, 오른쪽 끝)
    print(*numbers)