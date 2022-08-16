for t in range(1, int(input()) + 1):
    pole = input()
    # pole_cnt = 잘린 막대 개수, cnt = 현재 잘릴 막대 개수, idx = 탐색할 인덱스
    pole_cnt, cnt, idx = 0, 0, 0
    while idx < len(pole):
        # 레이저를 만나면 자르기
        if idx != len(pole) - 1 and pole[idx] + pole[idx + 1] == '()':
            pole_cnt += cnt
            idx += 1
        # 막대기가 끝나면 잘린 막대 개수 +1
        elif pole[idx] == ')':
            cnt -= 1
            pole_cnt += 1
        # 막대기가 시작하면 잘릴 맥대 개수 + 1
        else:
            cnt += 1
        idx += 1
    print(f'#{t} {pole_cnt}')
