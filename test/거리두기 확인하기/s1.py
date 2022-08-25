# 거리두기 확인하기

# def solution(places):
#     answer = []
#     return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

# places = [["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# 상, 하, 좌, 우, 좌상, 우하, 우상, 좌하, 상2, 하2, 좌2, 우2
d = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [1, 1],
    [-1, 1],
    [1, -1],
    [-2, 0],
    [2, 0],
    [0, -2],
    [0, 2],
]
answer = []
for place in places:
    breaker = False
    # 모두 탐색
    for row in range(5):
        if breaker:
            answer.append(0)
            break
        for col in range(5):
            if breaker:
                break
            # P찾으면
            if place[row][col] == 'P':
                for i in range(12):
                    nr = row + d[i][0]
                    nc = col + d[i][1]
                    # 맨해튼 거리 내P 찾으면
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        # 위 아래?
                        if row == nr:
                            btwn = abs(col - nc)
                            # 붙어있으면 지키지 x
                            if btwn == 1:
                                breaker = True
                                break
                            # 칸막이 조사
                            elif i == 8:
                                if place[nr][nc - 1] != 'X':
                                    breaker = True
                                    break
                            elif i == 9:
                                if place[nr][nc + 1] != 'X':
                                    breaker = True
                                    break

                        # 양 옆?
                        elif col == nc:
                            btwn = abs(row - nr)
                            # 붙어있으면 지키지 x
                            if abs(row - nr) == 1:
                                breaker = True
                                break
                            # 칸막이 조사
                            elif i == 10:
                                if place[nr + 1][nc] != 'X':
                                    breaker = True
                                    break
                            elif i == 11:
                                if place[nr - 1][nc] != 'X':
                                    breaker = True
                                    break

                        # 대각선
                        else:
                            # 칸막이 조사
                            if i == 4:
                                if place[nr][nc + 1] != 'X' or place[nr + 1][nc] != 'X':
                                    breaker = True
                                    break
                            elif i == 5:
                                if place[nr][nc - 1] != 'X' or place[nr - 1][nc] != 'X':
                                    breaker = True
                                    break
                            elif i == 6:
                                if place[nr][nc - 1] != 'X' or place[nr + 1][nc] != 'X':
                                    breaker = True
                                    break
                            elif i == 7:
                                if place[nr][nc + 1] != 'X' or place[nr - 1][nc] != 'X':
                                    breaker = True
                                    break
    if breaker:
        answer.append(0)
    else:
        answer.append(1)

print(answer)
