if __name__ == '__main__':
    text = input('Write text: ')
    sign = input('Write sign: ')
    text = text.lower()

    text_arr = text.split()

    for word in text_arr:
        for ch in word:
            if ch == sign:
                print(word)
