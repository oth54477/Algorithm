# 5174. subtree

# 자식 노드를 찾는 함수
def find_node(n):
    global depth
    # 재귀의 깊이를 누적해준다.
    depth += 1
    # 2씩 건너뛰며 현재 노드를 찾는다.
    for i in range(0, len(arr), 2):
        # arr[i]가 현재 노드일때
        if arr[i] == n:
            # 자식노드로 재귀함수를 돌린다.
            find_node(arr[i + 1])


for t in range(1, int(input()) + 1):
    depth = 0
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))

    v = e + 1
    # 찾고자 하는 노드n
    find_node(n)
    # 재귀의 깊이 == 노드의 개수
    print(f'#{t} {depth}')
