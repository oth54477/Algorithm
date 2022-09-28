import sys
from itertools import permutations

sys.stdin = open('input.txt')

def change(nums, m):
    if m == n:                                              # 최대 교환 횟수만큼 교환하면
        result.add(int(''.join(list(map(str,nums)))))       # result에 int형으로 추가하기
        return                                              # 재귀 탈출
    for case in permutations(list(range(len(nums))), 2):    # 요소 개수가 2인 순열 생성
        copy_nums = list(nums)                              # 리스트 카피
        copy_nums[case[0]], copy_nums[case[1]] = copy_nums[case[1]], copy_nums[case[0]] # 카드 바꿔주기
        int_cards = int(''.join(list(map(str,copy_nums))))  # int형으로 바꾸기
        if int_cards not in tmp[m]:                         # 중복 제거
            tmp[m].append(int_cards)                        # 중복 확인을 위해 리스트에 추가
            change(copy_nums, m+1)                          # 재귀
        

for t in range(1, int(input()) + 1):
    nums, n = map(str, input().split())
    n = int(n)
    nums = list(map(int, nums))
    result = set()
    tmp = [[] for _ in range(10)]
    change(nums, 0)
    print(f'#{t} {max(result)}')
