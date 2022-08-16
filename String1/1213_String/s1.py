for _ in range(10):
    t = int(input())
    find_text = input()
    text = input()
    # 찾고자 하는 문자열의 개수를 구한다.
    cnt = text.count(find_text)
    print(f'#{t} {cnt}')