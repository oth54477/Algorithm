table = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    for _ in range(n):
        # 문자열로 입력 받기
        line = input()
        # 입력 값에 1이 있을 때 암호 문자열
        if int(line) != 0:
            # 암호 문자열 변수에 저장
            real_line = line
    # 앞뒤의 0 지우기
    # line = str(int(str(int(real_line))[::-1]))[::-1]
    line = real_line.strip('0')
    # 문자열 길이가 7의 배수가 될 수 있게 앞에 0 붙이기
    line = ('0' * (7 - (len(line) % 7))) + line
    # 홀수, 짝수를 위한 cnt 변수, 잘못된 암호를 체크하기 위한 chk변수, 최종 값을 위한 result 변수 선언
    cnt, chk, result = 0, 0, 0
    for i in range(0, len(line), 7):
        cnt += 1
        # 압호 해독
        num = table[line[i : i + 7]]
        # 짝수일 때 chk에 더해주기
        if cnt % 2 == 0:
            chk += num
        # 홀수일 때 x3을 하고 더해주기
        else:
            chk += num * 3
        # result에 값 더하기
        result += num
    # chk값이 10의 배수가 아니면 잘못된 암호코드
    if chk % 10 != 0:
        result = 0

    print(f'#{t} {result}')
