n = int(input())

queue = []
result = []
# 큐에 카드의 숫자 넣기
for v in range(1, n + 1):
    queue.append(v)
while True:
    result.append(queue.pop(0))
    # result에 모든 카드가 들어가면 break
    if len(result) == n:
        break
    queue.append(queue.pop(0))

print(*result)
