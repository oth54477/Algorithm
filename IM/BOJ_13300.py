import math

n, k = map(int, input().split())

# 0으로 가득찬 7칸 배열 생성(0번째는 사용 x)
male = [0] * 7
female = [0] * 7

for _ in range(n):
    s, y = map(int, input().split())
    # 여학생
    if s == 0:
        female[y] += 1
    # 남학생
    else:
        male[y] += 1


cnt = 0
for i in range(1, 7):
    # 방의 수용인원(k)로 인원수를 나누고, 올림한다.
    cnt += math.ceil(female[i] / k)
    cnt += math.ceil(male[i] / k)
print(cnt)
