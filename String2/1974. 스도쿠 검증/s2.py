for t in range(int(input())):
    count = 1
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_reverse = list(map(list, zip(*sudoku)))  # 배열 뒤집기

    for line in range(9):
        if (
            len(set(sudoku[line])) != 9 or len(set(sudoku_reverse[line])) != 9
        ):  # 가로, 세로줄 검사
            count = 0
            break
    # n = 3                                           # box3개 검사할때마다 +3
    # m = 3                                           # box1개 검사마다 +3
    for box in range(3, 9, 3):  # box_line_1~3
        for box_num in range(3, 9, 3):  # box_1~3
            box_set = set()
            for row in range(box - 3, box):
                for col in range(box_num - 3, box_num):
                    box_set.add(sudoku[row][col])
            if len(box_set) != 9:
                count = 0
                break

    print(f'#{t+1} {count}')
