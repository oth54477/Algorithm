arr = [i for i in range(1, 13)]


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    result_count = 0
    for i in range(1 << 12):  # n의 제곱만큼 반복
        count = 0
        # i를 2진수로 바꾸고, 1의 개수를 탐색
        if format(i, 'b').count('1') == n:
            for j in range(12):
                # 부분집합 생성
                if i & (1 << j):  # i의 j번 비트가 1인 경우
                    # 부분집합의 합
                    count += arr[j]
            # 부분집합의 합이 k이면 최종 결과 + 1
            if count == k:
                result_count += 1
    print(f'#{tc} {result_count}')
