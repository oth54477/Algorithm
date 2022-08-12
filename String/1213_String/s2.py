for _ in range(10):
    t = int(input())
    find_text = input()
    text = input()
    cnt, find_len = 0, len(find_text)
    for idx in range(len(text) - find_len + 1):
        if text[idx : idx + find_len] == find_text:
            cnt += 1
    print(f'#{t} {cnt}')
