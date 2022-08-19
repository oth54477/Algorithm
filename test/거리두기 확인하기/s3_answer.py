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
                        # 바로 붙어있는 경우
                        if 0 <= i < 4:
                            breaker = True
                            break
                        # 상2
                        if i == 8:
                            if place[row + d[0][0]][col + d[0][1]] != 'X':
                                breaker = True
                                break
                        # 하2
                        elif i == 9:
                            if place[row + d[1][0]][col + d[1][1]] != 'X':
                                breaker = True
                                break

                        # 좌2
                        elif i == 10:
                            if place[row + d[2][0]][col + +d[2][1]] != 'X':
                                breaker = True
                                break
                        # 우2
                        elif i == 11:
                            if place[row + d[3][0]][col + +d[3][1]] != 'X':
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
