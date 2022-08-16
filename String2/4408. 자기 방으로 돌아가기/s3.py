import sys

sys.stdin = open('sample_input.txt')


for t in range(1, int(input()) + 1):
    n = int(input())
    # 0으로 가득찬 복도 리스트 생성
    paths = [0] * 201
    for _ in range(n):
        start, end = map(int, input().split())

        # 각각 방마다 복도 위치 설정
        if start % 2 == 0:
            # 위치가 짝수 -> 복도 = 위치 // 2
            start_path = start // 2
        else:
            # 홀수 -> 복도 = 위치 //2 + 1
            start_path = start // 2 + 1
        if end % 2 == 0:
            end_path = end // 2
        else:
            end_path = end // 2 + 1
        # 시작 위치의 방 번호가 더 클 경우 고려
        for idx in range(min(start_path, end_path), max(start_path, end_path) + 1):
            paths[idx] += 1

    print(f'#{t} {max(paths)}')
