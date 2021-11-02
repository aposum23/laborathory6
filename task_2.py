text = input('Write text: ')
text = text.lower()

for ind, ch in enumerate(text):
    if ind != 0:
        if ch == text[ind - 1]:
            print(f'Sign "{ch}" in positions {ind} and {ind + 1}')
