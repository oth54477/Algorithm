def solution(s):
    # 숫자 문자열을 인덱스와 일치하는 순서로 리스트로 저장한다.
    table = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]
    for idx, word in enumerate(table):
        if word in s:
            # 인덱스를 활용해 숫자 문자열을 해당하는 숫자로 바꾼다.
            s = s.replace(word, str(idx))
    return int(s)
