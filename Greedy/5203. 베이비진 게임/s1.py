import sys

sys.stdin = open('sample_input.txt')


def triplet(cards):
    arr = list(cards)
    arr.sort()
    cnt = 1
    for idx in range(len(arr) - 1):
        if arr[idx] == arr[idx + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt == 3:
            return True
    return False


def r(cards):
    arr = list(cards)  # cards의 자료형을 list로 바꾸고 arr변수에 저장한다.
    arr.sort()
    cnt = 1
    for i in range(len(arr) - 1):  # 0 과 1을 순서대로 i에 할당한다.
        if arr[i + 1] - arr[i] == 1:  # 다음 카드에서 현재 카드의 숫자를 빼서 1이면 run
            cnt += 1
        else:
            cnt = 1
        if cnt == 3:
            return True  # True 리턴
    return False


def chk(cards):
    if r(cards) or triplet(cards):
        return True
    else:
        return False


for t in range(1, int(input()) + 1):
    player1, player2 = [], []
    arr = list(map(int, input().split()))
    result = 0
    for i in range(0, len(arr), 2):
        player1.append(arr[i])
        player2.append(arr[i + 1])
        if len(player1) >= 3:
            if chk(player1):
                result = 1
        if len(player2) >= 3:
            if chk(player2):
                if result == 1:
                    result = 0
                    break
                result = 2
        if result==1 or result == 2:
            break
    else:
        result = 0
    print(f'#{t} {result}')
