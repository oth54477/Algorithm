# import time

# arr = [0, 4, 1, 3, 1, 2, 4, 1]

# # 버블 정렬
# start_time = time.time()
# for i in range(len(arr) - 1, 0, -1):
#     for idx in range(i):
#         if arr[idx] > arr[idx + 1]:
#             arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
# print('time :', time.time() - start_time)

# print(arr)


# arr2 = [0, 4, 1, 3, 1, 2, 4, 1]
# # 카운팅 정렬
# start_time = time.time()
# max_v = 0
# temp = [0] * (len(arr2))
# # 1. counter에 original 원소의 빈도수 담기
# for v in arr2:
#     if max_v < v:
#         max_v = v
# counts = [0] * (max_v + 1)
# # 2. 누적(counter 업데이트)
# for i in arr2:
#     counts[i] += 1
# # 3. result 생성
# for i in range(1, max_v + 1):
#     counts[i] += counts[i - 1]
# # 4. result에 정렬하기
# for j in arr2[::-1]:
#     counts[j] -= 1
#     temp[counts[j]] = j
# print('time :', time.time() - start_time)
# print(temp)
# 문자열 뒤집기

# s = 'abcdefgf'
# result = ''
# for i in range(len(s) - 1, -1, -1):
#     result += s[i]

# print(result)

# s = 'abcdefg'
# s = list(s)
# cnt = len(s) - 1
# print(s)
# for i in range(len(s) - 1, len(s) // 2, -1):
#     s[i], s[i - cnt] = s[i - cnt], s[i]
#     cnt -= 2

# print(s)


# 이진 탐색


def binarySearch(a, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
        return False
