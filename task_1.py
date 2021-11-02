text = input('Write text: ')
sign = input('Write sign: ')
text = text.lower()

textArr = text.split()

for word in textArr:
    for ch in word:
        if ch == sign:
            print(word)
