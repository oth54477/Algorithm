def success_rate(person, rate):
    global max_rate
    if person == n:                                                                     # 전부 계산하면
        max_rate = max(max_rate, rate)                                                  # 더 큰값 저장
        return
    if rate <= max_rate:                                                                # 백트래킹
        return
    for i in range(n):                                                                  # 모든 경우의 수 탐색
        if not visited[i]:                                                              # 아직 방문하지 않았으면
            visited[i] = True                                                           # 방문 처리
            success_rate(person + 1, rate * rate_arr[person][i])                        # 재귀 (다음사람, 비율, 방문)
            visited[i] = False                                                          # 방문 처리 해제



for t in range(1, int(input()) + 1):
    n = int(input())
    rate_arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]   # 100을 나눠서 리스트에 저장
    visited = [False] * n                                                               # 방문 리스트 생성
    max_rate = 0                                                                        # 최대값 저장할 변수
    success_rate(0, 1)                                                                  # 성공률 찾기
    print(f'#{t} {round(max_rate * 100, 6)  :.6f}')                                     # 소수점 6자리까지