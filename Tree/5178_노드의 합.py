# 5178_노드의 합

for t in range(1, int(input()) + 1):
    n, m, l = map(int, input().split())
    tree_arr = [0] * (n + 1)
    for _ in range(m):
        idx, value = map(int, input().split())
        # 트리 리스트에 리프노드들의 값을 입력해준다.
        tree_arr[idx] = value
    # 아래에서부터 올라오기 위해 for문을 반대로 돌려준다.
    for idx in range(n, 1, -1):
        # 현재 노드의 번호 //2는 부모 노드의 번호와 같다.
        # 부모 노드에 현재 노드의 값을 더해준다.
        tree_arr[idx // 2] += tree_arr[idx]
    print(f'#{t} {tree_arr[l]}')
