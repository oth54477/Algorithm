import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    # 치즈의 양
    cheese = list(map(int, input().split()))
    cnt, k = 0, n
    # 화덕에 n개의 피자를 넣는다.
    queue = cheese[:n]
    # 피자의 인덱스를 저장할 리스트
    idx = list(range(n))
    # n개의 피자가 들어갔다면, 이미 처음 들어간 피자는 한 바퀴 돌았다.
    queue[0] //= 2
    # 1개의 피자를 제외한 나머지 피자가 모두 0이 될 때 까지 반복
    while queue.count(0) != (n - 1):
        # 첫 번째 칸의 치즈가 0이고, k < m일때
        if queue[0] == 0 and k < m:
            # 새로운 피자 투입
            queue[0] = cheese[k]
            k += 1
            # cnt % n -> 꺼낸 피자의 idx리스트 에서의 인덱스
            idx[cnt % n] = k
        # 돌리기
        queue.append(queue.pop(0))
        # 치즈 반절
        queue[0] //= 2
        cnt += 1
    print(f'#{t}', idx[(cnt + queue.index(sum(queue))) % n])
