# words = input()

# # 크로아티아 알파벳을 리스트에 저장한다.
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# cnt = 0
# for alph in croatia:
#     if alph in words:
#         # 개수를 cnt에 더하고, 0으로 바꾼다.
#         cnt += words.count(alph)
#         words = words.replace(alph, '0')

# # 0을 지운다.
# words = words.replace('0', '')
# # 남은 문자의 개수를 cnt에 더한다.
# cnt += len(words)

# print(cnt)


words = input()

# 크로아티아 알파벳을 리스트에 저장한다.
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for alph in croatia:
    if alph in words:
        words = words.replace(alph, '0')


print(len(words))
