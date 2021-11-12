def find_char(str, chr, i):
    for ind, elem in enumerate(str):
        if elem == chr and ind != i:
            return True
    return False


if __name__ == '__main__':
    words = input('Write two words: ')
    words = words.replace(' ', '')
    words = words.lower()
    res_chars = ''

    for ind, ch in enumerate(words):
        if find_char(words, ch, ind):
            continue
        else:
            res_chars = res_chars + ch + ' '

    print(f'Result: {res_chars}')
