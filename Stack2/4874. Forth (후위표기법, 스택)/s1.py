for t in range(1, int(input()) + 1):
    forth_code = input().split()
    stack = []
    for e in forth_code:
        # 문자열이 숫자일 때 int형으로 스택에 push
        if e.isdigit():
            stack.append(int(e))
 
        elif len(stack) < 2:
            print(f'#{t} error')
            break
        else:
            # 연산자를 만나면 두개의 요소를 pop해 알맞는 연산 진행 후 스택에 push
            pop1 = stack.pop()
            pop2 = stack.pop()
            if e == '+':
                stack.append(pop2 + pop1)
            elif e == '-':
                stack.append(pop2 - pop1)
            elif e == '*':
                stack.append(pop2 * pop1)
            elif e == '/':
                stack.append(pop2 // pop1)
