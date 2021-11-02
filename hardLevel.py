def findChar(str, ch, i):
    for ind, elem in enumerate(str):
        if elem == ch and ind != i:
            return True
    return False


words = input('Write two words: ')
words = words.replace(' ', '')
words = words.lower()
resChars = ''

for ind, ch in enumerate(words):
    if findChar(words, ch, ind):
        continue
    else:
        resChars = resChars + ch + ' '

print(f'Result: {resChars}')
