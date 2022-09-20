# 5176. 이진탐색

# 중위순회
def inorder(node):
    global cnt
    if node <= n:
        inorder(node * 2)
        # 노드에 맞는 값을 1부터 순서대로 입력
        tree_arr[node] = cnt
        cnt += 1
        inorder(node * 2 + 1)


for t in range(1, int(input()) + 1):
    n = int(input())
    cnt = 1
    tree_arr = [0] * (n + 1)

    inorder(1)
    print(f'#{t} {tree_arr[1]} {tree_arr[n//2]}')
