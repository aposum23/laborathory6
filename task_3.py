text = input('Write text: ')
text = text.lower()
resText = ''

for ind, ch in enumerate(text):
    if (ch == 'o' and ind % 2 == 0) or (ch == 'о' and ind % 2 == 0):
        continue
    else:
        resText = resText + ch

print(f'Reformed text: {resText}')
