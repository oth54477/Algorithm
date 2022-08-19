# 7675. 통역사 성경이

for t in range(1, int(input()) + 1):
    n = int(input())

    words = input()
    print(f'#{t}', end=' ')
    arr = words.replace('!', '.').replace('?', '.').split('.')
    cnt = 0
    for s in arr:
        s = s.strip()
        if s == '':
            continue
        check_arr = s.split()
        for s2 in check_arr:
            if not s2[0].isupper():
                continue
            for s3 in s2[1:]:
                if not s3.islower():
                    break

            else:
                cnt += 1
        else:
            print(cnt, end=' ')
            cnt = 0
    print()
