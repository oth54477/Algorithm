for t in range(1, int(input()) + 1):
    word1 = input()
    word2 = input()
    # word1이 word2에 포함 유무 확인
    if word1 in word2:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)
