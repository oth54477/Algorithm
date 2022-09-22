import sys
from itertools import permutations

sys.stdin = open('input.txt')

def change(arr, m):
    # price = int(''.join(list(map(str,arr))))
    
    if m == n+1:
        result.add(int(''.join(list(map(str,arr)))))
        return
    a = list(arr)
    for case in permutations(list(range(len(a))), 2):
        a[case[0]], a[case[1]] = a[case[1]], a[case[0]]
        change(a, m+1)
        

for t in range(1, int(input()) + 1):
    info, n = map(str, input().split())
    n = int(n)
    info = list(map(int, info))
    result = set()
    change(info, 0)
    print(f'#{t} {max(result)}')
