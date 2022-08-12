# 얼굴을 기준으로 l,r을 나눈다.
l, r = input().split('(^0^)')

# l과 r에서 @의 개수를 구한다.
l_punch = l.count('@')
r_punch = r.count('@')

print(l_punch, r_punch)