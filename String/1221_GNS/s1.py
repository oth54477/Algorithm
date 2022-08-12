# 어느 행성의 숫자를 table 리스트에 인덱스와 일치하는 순서로 저장한다.
table = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, int(input()) + 1):
    tc, n = map(str, input().split())
    arr = input().split()

    # 숫자별 개수를 구하기 위한 cnt_arr리스트를 만든다.
    cnt_arr = [0] * 10
    for idx, word in enumerate(table):
        # 개수를 구하고, 리스트에 더한다.
        cnt_arr[idx] += arr.count(word)

    print(tc)
    for i in range(10):
        # 어느 행성의 숫자의 개수를 작은순서로 개수와 곱해 출력한다.
        print((table[i] + ' ') * cnt_arr[i], end='')
