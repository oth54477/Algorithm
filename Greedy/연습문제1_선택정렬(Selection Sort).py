# 연습문제1. 선택정렬(Selection Sort)


# def selection_sort(i, n):
#     if i == n - 1:
#         return
#     min_num = max(numbers)
#     for j in range(i, n):
#         if numbers[j] < min_num:
#             min_num = numbers[j]
#             min_index = j
#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
#     selection_sort(i + 1, n)


def selection_sort(arr):
    l = len(arr)
    for i in range(l):
        min_num = max(arr)
        for j in range(i, l):
            if arr[j] < min_num:
                min_num = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(numbers)
print(numbers)
