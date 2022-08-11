for tc in range(1, 11):
    width = int(input())
    building = list(map(int, input().split()))
    
    view = 0
    # 5칸씩 나눠서 양 옆 각각 2칸의 빌딩 높이 확인
    for idx in range(width - 2):
        check_arr = building[idx:idx+5]
        max_height, second_height = 0, 0
        # 가장 큰 높이와 두 번째 높이 찾기
        for height in check_arr:
            if height > max_height:
                second_height, max_height = max_height, height
            elif height > second_height:
                second_height = height
        # 가운데 있는 빌딩의 높이가 가장 높다면
        if max_height == check_arr[2]:
            # 두번째 높은 빌딩과의 높이차 = 조망권 확보 세대
            view += (max_height - second_height)
    print(f'#{tc} {view}')