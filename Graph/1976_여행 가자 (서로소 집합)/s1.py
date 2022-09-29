import sys

input = sys.stdin.readline

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

n = int(input())
m = int(input())
parent = list(range(n))
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            x_root, y_root = find_set(i), find_set(j)
            if x_root != y_root:
                if x_root < y_root:
                    parent[y_root] = x_root
                else:
                    parent[x_root] = y_root
                    
plan = set(map(lambda x: parent[int(x) - 1], input().split()))  # 계획들 사이에 길이 있는지 확인
if len(plan) == 1:                                              # 집합의 길이가 1이면 길이 있다.
    print('YES')
else:                                                           # 1 이상이면 연결되지 않은 부분이 있다.
    print('NO')
