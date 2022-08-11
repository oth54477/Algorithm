T = int(input())

for tc in range(1, 1+T):
    cards = input()
    
    result, idx = 0, 0
    counts = [0 for _ in range(10)]
    for card in cards:  # 숫자별 카드 개수 확인
        counts[int(card)] += 1
    
    while idx < 10:
        if counts[idx] >= 3:        # triplet인 경우
            result += 1
            counts[idx] -= 3
        elif counts[idx] > 0 and counts[idx+1] > 0 and counts[idx+2] > 0:   # run인 경
            result += 1
            counts[idx] -= 1
            counts[idx+1] -= 1
            counts[idx+2] -= 1
        else:
            idx += 1
            
    if result == 2: # baby-gin인 경우
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')