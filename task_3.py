if __name__ == '__main__':
    text = input('Write text: ')
    text = text.lower()
    res_text = ''

    for ind, ch in enumerate(text):
        if (ch == 'o' and ind % 2 == 0) or (ch == 'о' and ind % 2 == 0):
            continue
        else:
            res_text = res_text + ch

    print(f'Reformed text: {res_text}')
