# 연습문제2. Baby gin

from itertools import permutations                  # 부분집합을 만들기 위한 라이브러리
import copy                                         # 딥카피를 이용하기 위한 라이브러리


def triplet(cards):                                 # triplet인지 확인하기 위한 함수 선언 (중복되는 숫자 세장)
    if len(set(cards)) == 1:                        # 자료형을 set으로 바꿨을 떼 중복되는 숫자는 사라진다. -> 길이가 1이면 triplet
        return True                                 # True를 리턴한다.
    else:                                           # triplet이 아니면
        return False                                # False 리턴


def run(cards):                                     # run인지 확인하기 위한 함수 선언 (연속되는 숫자 세장)
    arr = list(cards)                               # cards의 자료형을 list로 바꾸고 arr변수에 저장한다.
    arr.sort()                                      # 리스트 정렬
    for i in range(2):                              # 0 과 1을 순서대로 i에 할당한다.
        if arr[i + 1] - arr[i] == 1:                # 다음 카드에서 현재 카드의 숫자를 빼서 1이면 run
            return True                             # True 리턴
    else:                                           # run이 아니면
        return False                                # False 리턴


def other_cards(cards, card_3):                     # 초기 6장의 카드(cards)에서 card_3의 카드 3장을 제외한 카드들을 구하는 함수
    tmp = copy.deepcopy(cards)                      # 딥 카피로 cards를 복사해 tmp에 저장
    for card in card_3:                             # card_3의 카드들을 하나씩 card에 할당
        tmp.remove(card)                            # tmp에서 해당 카드를 하나씩 제거
    return tmp                                      # 3장의 카드가 저장된 tmp변수를 리턴


for t in range(1, int(input()) + 1):
    cards = list(map(int, input()))
    result = False
    for card_3 in permutations(cards, 3):           # permutations(리스트, 요소 개수)함수를 활용해 지정된 개수의 요소를 갖는 튜플 반환
        if triplet(card_3) or run(car_3):           # 뽑은 카드들이 triplet이거나 run인지 확인
            others = other_cards(cards, card_3)     # triplet이거나 run이면 other_cards(전체카드, 제외카드)를 활용해 나머지 카드를 others변수에 저장
            if triplet(others) or run(others):      # 나머지 카드들이 triplet이거나 run인지 확인
                result = True                       # triplet이거나 run이면 True
                break                               # for문 탎출

    print(f'#{t} {result}')


for tc in range(1, int(input()) + 1):
    cards = input()

    result, idx = 0, 0
    counts = [0 for _ in range(10)]
    for card in cards:  # 숫자별 카드 개수 확인
        counts[int(card)] += 1

    while idx < 10:
        if counts[idx] >= 3:  # triplet인 경우
            result += 1
            counts[idx] -= 3
        elif counts[idx] > 0 and counts[idx + 1] > 0 and counts[idx + 2] > 0:  # run인 경
            result += 1
            counts[idx] -= 1
            counts[idx + 1] -= 1
            counts[idx + 2] -= 1
        else:
            idx += 1

    if result == 2:  # baby-gin인 경우
        result = True
    else:
        result = False
    print(f'#{tc} {result}')
