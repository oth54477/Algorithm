import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    cnt = 1
    rooms = [0] * 400
    for _ in range(n):
        status = False
        start, end = map(int, input().split())
        if start % 2 == 0:
            start -= 1
        if end % 2 == 0:
            end -= 1
        # if start <= end:
        #     move = range(start, end + 2, 2)
        # else:
        #     move = range(end, start - 2, -2)
        if start <= end:
            for idx in range(start, end + 2, 2):
                if status == False and rooms[idx] != 0:
                    cnt += 1
                    status = True
                if idx + 2 < 400 and rooms[idx + 2] == 0:
                    status = False
                rooms[idx] += 1

        else:
            for idx in range(end, start - 2, -2):
                if status == False and rooms[idx] != 0:
                    cnt += 1
                    status = True
                if idx + 2 < 400 and rooms[idx - 2] == 0:
                    status = False
                rooms[idx] += 1
    print(f'#{t} {cnt}')
