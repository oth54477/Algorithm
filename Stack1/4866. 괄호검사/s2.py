# 괄호 테이블
table = {'}': '{', ')': '('}

for t in range(1, int(input()) + 1):
    s = input()
    print(f'#{t}', end=' ')
    stack = []
    for i in s:
        # stack에 push
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}' or i == ')':
            # 빈 stack인 경우 break
            if not stack:
                break
            else:
                pop1 = stack.pop()
                # 짝이 안맞는 경우 break
                if pop1 != table[i]:
                    break

    else:
        print(1) if not stack else print(0)
        continue

    print(0)
