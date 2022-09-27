def move(location, charge):
    global min_charge
    battery = stations[location]                # 배터리 교체
    charge += 1                                 # 충전 횟수 + 1
    if charge >= min_charge:                    # 백트래킹
        return
    if location + battery >= n-1:               # 최대 이동거리만큼 이동했을 때 도착하면
        min_charge = min(min_charge, charge)    # 최소 충전 횟수 저장
        return                                  # 재귀 탈출
    for i in range(battery, 0, -1):             # 갈 수 있는 경우의 수 모두 확인 
        move(location + i, charge)
        
for t in range(1, int(input()) + 1):
    n, *stations = map(int, input().split())
    min_charge = n * n                          # 최대 충전 횟수
    move(0, -1)                                 # 이동하는 함수 처음 위치는 횟수 x이기 때문에 -1에서 시작
    print(f'#{t} {min_charge}') 