# 5189. 전자카트
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# import sys
# from itertools import permutations
# 
# sys.stdin = open('input.txt')
# 
# for t in range(1, int(input()) + 1):
#     n = int(input())
#     field = [list(map(int, input().split())) for _ in range(n)]
#     
#     arr = set()                                             # 중복을 제거하기 위해 set 자료형 사용
#     for case in permutations(list(range(1, n)), n-1):       # 1~n까지의 숫자가 들어있는 리스트에서 길이 n-1인 순열 만들기
#         arr.add(tuple([0] + list(case) + [0]))              # 앞뒤로 0을 붙이고 set에 추가 
#             
#     result = []                                             # 각각 경우의 합을 저장할 result 리스트
#     for path in arr:                                        # arr(set 자료형)에 있는 순열들을 하나씩 path에 할당
#         sum_num = 0                                         # sum_num을 0으로 초기화
#         for idx in range(len(path)-1):                      # for문으로 인덱스 하나씩 할당
#             sum_num += field[path[idx]][path[idx+1]]        # sum_num에 배터리 소모량 하나씩 더하기
#         result.append(sum_num)                              # result에 추가
#     print(f'#{t} {min(result)}')                            # result에서 가장 작은 값
#             


import sys
from itertools import permutations

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]
    result = 100 * 100                                      # result를 최대한 큰 값으로 초기화
    for case in permutations(list(range(1, n)), n - 1):     # 1~n까지의 숫자가 들어있는 리스트에서 길이 n-1인 순열 만들기
        path = [0] + list(case) + [0]                       # 순열에 앞뒤로 0을 붙여 path 생성
        sum_num = 0
        for idx in range(len(path) - 1):                    # for문으로 인덱스 할당
            sum_num += field[path[idx]][path[idx + 1]]      # 배터리 사용량 더하기
        result = min(result, sum_num)                       # 더 작은 값이 result
    print(f'#{t} {result}')
            
        




