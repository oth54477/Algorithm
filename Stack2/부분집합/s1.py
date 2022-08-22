def powerset(arr, depth, total):
    if total > 10:
        return

    if depth == len(numbers):
        if total == 10:
            print(arr)
        return

    powerset(arr + [number[depth]], depth + 1, total + numbers[depth])

    powerset(arr, depth + 1, total)


number = list(range(1, 11))
powerset([], 0, 0)
