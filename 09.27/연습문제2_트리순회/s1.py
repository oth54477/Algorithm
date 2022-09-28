def preorder(node):                 # 전위 순회 (VLR)
    if node != 0:                   # 노드가 0이 아닐 때
        child = graph[node]         # 자식 노드 번호 받아오기
        pre_arr.append(node)        # 부모노드 리스트에 저장
        if child:                   # 리스트에 값이 있으면
            preorder(child[0])      # 왼쪽 자식 재귀
        if len(child) == 2:         # 자식 노드가 2개 일 때
            preorder(child[1])      # 오른쪽 자식 재귀

def inorder(node):                  # 중위 순회 (LVR)
    if node != 0:
        child = graph[node]
        if child:
            inorder(child[0])
        in_arr.append(node)
        if len(child) == 2:
            inorder(child[1])

def postorder(node):                # 후위 순회 (LRV)
    if node != 0:
        child = graph[node]
        if child:
            postorder(child[0])
        if len(child) == 2:
            postorder(child[1])
        post_arr.append(node)


v, e = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(v + 1)]

for idx in range(0, len(arr)-1, 2):
    graph[arr[idx]].append(arr[idx+1])

pre_arr, in_arr, post_arr = [], [], []
preorder(1)                         # 전위 순회
inorder(1)                          # 중위 순회
postorder(1)                        # 후위 순회
print('전위 순회 : ', *pre_arr)
print('중위 순회 : ', *in_arr)
print('후위 순회 : ', *post_arr)