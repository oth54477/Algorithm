# import sys

# sys.stdin = open('sample_input.txt')


def bfs(s):
    visited[s] = True
    queue = [[s, 0]]
    min_cnt = v + 1
    # 시작 노드와 도착 노드가 같을 경우
    if s == g:
        return 0
    while queue:
        sp, cnt = queue.pop(0)
        cnt += 1
        for next_p in graph[sp]:
            # 도착했을 경우 cnt 리턴
            if next_p == g:
                return cnt
            if not visited[next_p]:
                visited[next_p] = True
                queue.append([next_p, cnt])


for t in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    s, g = map(int, input().split())

    visited = [False] * (v + 1)

    result = bfs(s)
    if result == None:
        print(f'#{t} 0')
    else:
        print(f'#{t} {result}')
