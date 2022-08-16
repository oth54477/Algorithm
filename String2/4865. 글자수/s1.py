for t in range(1, int(input()) + 1):
    word1 = input()
    word2 = input()
    max_cnt = 0
    # word1의 한 문자씩 s에 할당
    for s in word1:
        # word2에서 s의 개수 구하기
        cnt = word2.count(s)
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{t} {max_cnt}')
