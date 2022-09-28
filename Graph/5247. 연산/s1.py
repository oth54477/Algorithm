from collections import deque
table = {0: lambda x: x+1, 1: lambda x: x-1, 2: lambda x: x*2, 3:lambda x: x-10}

def bfs(num):
    q = deque([[num, 0]])
    while True:
        num, cnt = q.popleft()
        if num not in chk:                                          # 여기서 확인 안하면 7번째에서 시간초과..
            chk.add(num)
            for i in range(4):                                      # 4가지 연산 진행
                new_num = table[i](num)                             # 키값에 맞는 연산 결과 변수에 저장
                if new_num == m:                                    # 목표 값 찾으면
                    return cnt + 1                                  # cnt + 1 리턴 ( 마지막 연산 횟수 포함)
                if new_num not in chk and 0 <= new_num <= 1000000:  # 범위 안이고, 이미 계산한 값이 아니면
                    q.append([new_num, cnt + 1])                    # 덱에 추가

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    chk = set()
    result = bfs(n)
    print(f'#{t} {result}')

#
# table = {0: lambda x: x-1, 1: lambda x: x+1, 2: lambda x: x/2, 3:lambda x: x+10}
#
# def bfs(num):
#     q = deque([[num, 0]])
#     while True:
#         num, cnt = q.popleft()
#         chk.add(num)
#         for i in range(4):
#             new_num = table[i](num)
#             if new_num == n:
#                 return cnt + 1
#             if new_num.is_integer() and new_num not in chk and 0 < new_num <= 1000000:
#                 q.append([new_num, cnt + 1])


# def bfs(num):
#     cnt = 0
#     while True:
#         if num * 2 > m:
#             break
#         num *= 2
#         cnt += 1
#     num2 = num * 2
#     cnt2 = cnt + 1
#     a = m - num
#     b = abs(num2 - m)
#     cnt += a % 2 + a//2
#     print(cnt2, (10 -(b % (2**cnt2))), b //(2**cnt2))
#     cnt2 += 1 + (10 -(b % (2**cnt2))) + b //(2**cnt2)
#     return min(cnt, cnt2)




