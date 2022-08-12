word = input()

word_filter = 'CAMBRIDGE'

# 문자열의 문자를 하나씩 alph에 할당하며 word에서 지운다.
for alph in word_filter:
    word = word.replace(alph, '')
print(word)
