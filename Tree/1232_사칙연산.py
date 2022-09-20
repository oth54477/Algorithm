# 1232. 사칙연산

# lambda함수를 이용해서 사칙연산을 수행한다.
# (lambda x, y: x + y)(10,20)은 10+20의 결과인 30을 반환함을 활용한다.
cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}
for t in range(1, 11):
    n = int(input())
    # 연산자에 int를 하면 에러가 발생하기때문에 예외처리를 한다.
    # map에서 lambda와 isdigit()함수를 활용해 숫자 여부를 확인 후 숫자면 int, 아니면 문자열로 저장한다.
    arrs = [
        list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        for _ in range(n)
    ]
    tree_arr = [0] * (n + 1)

    for arr in arrs[::-1]:
        # 리스트의 길이가 2이면 리프노드이므로 저장한다.
        if len(arr) == 2:
            tree_arr[arr[0]] = arr[1]
        # 그 외의 경우는 사칙연산을 진행한다.
        else:
            # ex) '+'인 경우 -> 부모노드 = lambda x, y: x + y(왼쪽 자식노드, 오른쪽 자식노드)
            tree_arr[arr[0]] = cal[arr[1]](tree_arr[arr[2]], tree_arr[arr[3]])

    print(f'#{t} {tree_arr[1]}')
