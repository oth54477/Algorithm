# def partition(arr, left, right):
#     pivot = arr[left]  # 가장 왼쪽 원소를 피벗으로 지정
#     i, j = left, right
# 
#     while i <= j:
#         # 1. 피벗보다 큰 값이 나올 때까지 i + 1
#         while i <= j and arr[i] <= pivot:
#             i += 1
# 
#         # 2. 피벗보다 작은 값이 나올 때까지 j - 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
# 
#         # 3. 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 교환
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
# 
#     arr[left], arr[j] = arr[j], arr[left]  # i > j가 되면 피벗과 j 위치 원소 교환 (피벗을 가운데로 옮기는 작업)
# 
#     return j
# 
# 
# def quick_sort(arr, left, right):
#     if left < right:
#         middle = partition(arr, left, right)  # 피벗을 기준으로 왼쪽, 오른쪽을 나누는 가운데 위치 구하기
#         quick_sort(arr, left, middle - 1)  # 왼쪽 퀵정렬
#         quick_sort(arr, middle + 1, right)  # 오른쪽 퀵정렬
# 
# 
# for t in range(1, int(input()) + 1):
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     quick_sort(numbers, 0, len(numbers) - 1)
#     print(f'#{t} {numbers[n//2]}')
#     


def partition(arr, left, right):                # 분할할 위치 찾기
    pivot = arr[left]                           # 맨 왼쪽이 피벗 -> 호어 방식
    i, j = left, right                          # i와 j 는 왼쪽 오른쪽
    while i <= j:                               # i와 j가 교차할 때까지 반복
        while i <= j and arr[i] <= pivot:       # 교차x, i위치의 값이 피벗보다 큰 위치 찾기
            i += 1                              # 못찾으면 오른쪽으로 한칸 이동
        while i <= j and arr[j] >= pivot:       # 교차x, j위치의 값이 피벗보다 작은 위치 찾기
            j -= 1                              # 못찾으면 욑쪽으로 한칸 이동
        if i < j:                               # 교차하면
            arr[i], arr[j] = arr[j], arr[i]     # 서로 값 바꾸기
    arr[left], arr[j] = arr[j], arr[left]       # 피벗과 j의 값 바꾸기
    return j                                    # j를 middle로 저장하기 위해 반환

def quick_sort(arr, left, right):               # 퀵 정렬 -> 리스트, 왼쪽 인덱스, 오른쪽 인덱스를 입력받는다.
    if left < right:                            
        middle = partition(arr, left, right)    # 중간 위치 찾기(피벗의 인덱스)
        quick_sort(arr, left, middle - 1)       # 왼쪽 리스트 정렬
        quick_sort(arr, middle + 1, right)      # 오른쪽 리스트 정렬

for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, n-1)                 # 퀵 정렬
    print(f'#{t} {numbers[n // 2]}')