# 5177. 이진 힙

# for t in range(1, int(input()) + 1):
#     n = int(input())
#     tree_arr = [0] + list(map(int, input().split()))

#     find_change = True
#     while find_change:
#         find_change = False
#         for idx in range(2, n + 1):
#             parent, child = idx // 2, idx

#             if tree_arr[parent] > tree_arr[child]:
#                 tree_arr[parent], tree_arr[child] = tree_arr[child], tree_arr[parent]
#                 find_change = True

#     result = 0
#     while n > 1:
#         n //= 2
#         result += tree_arr[n]
#     print(f'#{t} {result}')

for t in range(1, int(input()) + 1):
    n = int(input())
    tree_arr = [0] + list(map(int, input().split()))

    for idx in range(2, n + 1):
        parent, child = idx // 2, idx
        # 루트 노드까지 대소비교
        while parent != 0:
            # 자식이 부모보다 작으면 서로 바꿔준다.
            if tree_arr[parent] > tree_arr[child]:
                tree_arr[parent], tree_arr[child] = tree_arr[child], tree_arr[parent]
            parent, child = parent // 2, parent

    result = 0
    # 조상노드를 찾는다.
    while n > 1:
        n //= 2
        result += tree_arr[n]
    print(f'#{t} {result}')
