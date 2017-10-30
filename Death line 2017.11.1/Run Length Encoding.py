"""run Lenght Encoding"""
def encoding(word, ref, count, encoded):
    """encoding word"""
    for i in word:
        if i == ref:
            count += 1
            ref = i
            encoded = str(count)+i
        else:
            print(encoded, end='')
            count = 1
            ref = i
            encoded = str(count)+i
    print(encoded)
encoding(input(), '', 0, '')
