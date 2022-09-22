import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    result = 0
    weights.sort(reverse=True)      # 화물 무게 내림차순 정렬    
    trucks.sort()                   # 트럭 적재량 오름차순 정렬
    for w in weights:               # 화물의 무게를 하나씩 할당
        for idx in range(m):        # 트럭의 적재량과 비교하기 위해 인덱스 할당
            if w <= trucks[idx]:    # 트럭에 화물이 적재 가능하면
                result += w         # result에 더해준다.
                trucks[idx] = 0     # 적재량을 0으로 바꾼다.
                break               # for문 탈출
    print(f'#{t} {result}')

                
    
