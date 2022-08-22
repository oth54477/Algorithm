table = {'{': '}', '(': ')'}

for t in range(1, int(input()) + 1):
    s = input()
    print(f'#{t}', end=' ')
    stack = []
    for i in s:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}' or i == ')':
            if not stack:
                break
            else:
                if i == '}':
                    if stack.pop() != '{':
                        break
                elif i == '}':
                    if stack.pop() != '(':
                        break
                else:
                    stack.pop()

    else:
        if not stack:
            print(1)
        else:
            print(0)
        continue

    print(0)
