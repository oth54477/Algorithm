# 2819. 격자판의 숫자 이어 붙이기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB

import sys

sys.stdin = open('sample_input.txt')

def dfs(row, col, s):
    if len(s) == 7:                             # 문자의 길이가 7일때
        nums_set.add(s)                         # set에 추가
        return                                  # 재귀 탈출
        
    for d in range(4):                          # 4방향 델타 이동
        nr, nc = row + dx[d], col + dy[d]       # 이동 좌표
        if 0<= nr < 4 and 0<= nc < 4:           # 범위 벗어나지 않을 때
            dfs(nr,nc,s+str(arr[nr][nc]))       # 문자열에 추가하고 재귀
            

dx = [-1, 1, 0, 0]                              # 상, 하, 좌, 우
dy = [0, 0, -1, 1]                              # 상, 하, 좌, 우
for t in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    nums_set = set()                            # set에 저장해 중복 제거
    for row in range(4):                        # 열 완전 탐색
        for col in range(4):                    # 행 완전탐색
            dfs(row, col,'')                    # dfs
    
    print(f'#{t} {len(nums_set)}')
