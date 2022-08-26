# 1289. 원재의 메모리 복구하기

for t in range(1, int(input()) + 1):
    bit = str(int(input()))

    old_char = False
    cnt = 1
    for char in bit:
        if not old_char:
            old_char = char
            continue
        elif old_char != char:
            cnt += 1
        old_char = char
    print(cnt)
