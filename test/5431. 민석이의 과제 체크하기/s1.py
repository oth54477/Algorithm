# 5431. 민석이의 과제 체크하기
for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    homework = list(map(int, input().split()))
    student = []
    for i in range(1, n + 1):
        student.append(i)
    result = list(set(student) - set(homework))
    print(f'#{t}', *result)
