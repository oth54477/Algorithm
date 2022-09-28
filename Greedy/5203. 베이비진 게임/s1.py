# import sys
#
# sys.stdin = open('sample_input.txt')
#
#
# def triplet(cards):
#     arr = list(cards)
#     arr.sort()
#     cnt = 1
#     for idx in range(len(arr) - 1):
#         if arr[idx] == arr[idx + 1]:
#             cnt += 1
#         else:
#             cnt = 1
#         if cnt == 3:
#             return True
#     return False
#
#
# def run_3(cards):
#     arr = list(set(cards))  # cards의 자료형을 list로 바꾸고 arr변수에 저장한다.
#     arr.sort()
#     cnt = 1
#     for i in range(len(arr) - 1):  # 0 과 1을 순서대로 i에 할당한다.
#         if arr[i + 1] - arr[i] == 1:  # 다음 카드에서 현재 카드의 숫자를 빼서 1이면 run
#             cnt += 1
#         else:
#             cnt = 1
#         if cnt == 3:
#             return True  # True 리턴
#     return False
#
#
# def chk(cards):
#     if run_3(cards) or triplet(cards):
#         return True
#     return False
#
#
# for t in range(1, int(input()) + 1):
#     player1, player2 = [], []
#     card_arr = list(map(int, input().split()))
#     result = 0
#     for i in range(0, len(card_arr), 2):
#         player1.append(card_arr[i])
#         player2.append(card_arr[i + 1])
#         if len(player1) >= 3:
#             if chk(player1):
#                 result = 1
#                 break
#         if len(player2) >= 3:
#             if chk(player2):
#                 result = 2
#                 break
#     print(f'#{t} {result}')




import sys

sys.stdin = open('sample_input.txt')

# 가지고 있는 카드가 triplet인지 확인하는 함수
def triplet(cards):
    if 3 in cards:      # 3이 카드목록 리스트 안에 있으면
        return True     # True
    return False        # 없으면 False

# 가지고 있는 카드가 run인지 확인하는 함수
def run_3(cards):
    for idx in range(len(cards) - 2):                       # 범위 초과를 막기 위해 길이 -2 만큼 반복
        if cards[idx] and cards[idx+1] and cards[idx+2]:    # 연속된 세개의 카드가 1장이상 있으면
            return True                                     # True 리턴
    return False                                            # 없으면 False 리턴


# 가지고 있는 카드가 run 혹은 triplet인지 확인하는 함수
def chk(cards):
    if run_3(cards) or triplet(cards):          # run 혹은 triplet이면
        return True                             # True 리턴
    return False                                # 아니면 False 리턴


for t in range(1, int(input()) + 1):
    player1, player2 = [0] * 10, [0] * 10       # 0~10을 저장할 수 있는 리스트 생성
    card_arr = list(map(int, input().split()))
    result, cnt = 0, 0
    for i in range(0, len(card_arr), 2):
        cnt += 1                                # 플레이어1, 2의 카드 수
        player1[card_arr[i]] += 1               # 카드의 숫자 인덱스의 값 + 1
        player2[card_arr[i + 1]] += 1           # 카드의 숫자 인덱스의 값 + 1
        if cnt >= 3:                            # 카드가 3장 이상일 때
            if chk(player1):                    # 플레이어 1이 run 혹은 triplet인지 확인
                result = 1                      # 맞으면 result는 1
                break                           # 반복문 탈출
            if chk(player2):                    # 플레이어 2이 run 혹은 triplet인지 확인
                result = 2                      # 맞으면 result는 2
                break                           # 반복문 탈출
    print(f'#{t} {result}')
