import sys

sys.stdin = open('input.txt')


def chk(arr):
    if len(set(arr)) == 9:
        return 1
    return 0


for t in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_chk = 0 if 0 in set(map(chk, sudoku)) else 1
    if not sudoku_chk:
        print(f'#{t} {0}')
        continue
    sudoku_reverse = list(map(list, zip(*sudoku)))
    reverse_chk = 0 if 0 in set(map(chk, zip(*sudoku))) else 1
    if not reverse_chk:
        print(f'#{t} {0}')
        continue
    box = []
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            box.append(
                sudoku[row][col : col + 3]
                + sudoku[row + 1][col : col + 3]
                + sudoku[row + 2][col : col + 3]
            )
    box_chk = 0 if 0 in set(map(chk, box)) else 1
    if not box_chk:
        print(f'#{t} {0}')
        continue
    print(f'#{t} {1}')
