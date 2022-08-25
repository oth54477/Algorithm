# 우선순위 설정
priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, ')': 1}
for t in range(1, 11):
    n = int(input())
    formula = input()
    postfix = ''
    stack = []

    for v in formula:
        # 문자가 숫자일 때
        if v.isdigit():
            # 문자열에 바로 추가
            postfix += v
        else:
            if stack:
                if v == ')':
                    while stack and stack[-1] != '(':
                        postfix += stack.pop()
                    stack.pop()
                # 스택 top과 비교하여 우선순위가 낮을때
                elif priority[stack[-1]] >= priority[v] and v != '(':
                    # 더 우선순위가 낮은 연산자를 만날 때 까지 pop
                    while (
                        stack
                        and priority[stack[-1]] >= priority[v]
                        and stack[-1] != '('
                    ):
                        postfix += stack.pop()
            # stack에 push
            if v != ')':
                stack.append(v)
    # 스택에 남은 것들을 모두 pop해 문자열에 추가
    while stack:
        postfix += stack.pop()
    stack2 = []
    for e in postfix:
        # 문자열이 숫자일 때 int형으로 스택에 push
        if e.isdigit():
            stack2.append(int(e))
        else:
            # 연산자를 만나면 두개의 요소를 pop해 알맞는 연산 진행 후 스택에 push
            pop1 = stack2.pop()
            pop2 = stack2.pop()
            if e == '+':
                stack2.append(pop2 + pop1)
            elif e == '-':
                stack2.append(pop2 - pop1)
            elif e == '*':
                stack2.append(pop2 * pop1)
            elif e == '/':
                stack2.append(pop2 / pop1)
    # 마지막에 남은 요소가 결과값
    print(f'#{t} {stack2.pop()}')
