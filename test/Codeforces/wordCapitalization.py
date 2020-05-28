#3m
word = [ch for ch in input()]
if word[0].islower():
    word[0] = word[0].upper()
print(''.join(word))

