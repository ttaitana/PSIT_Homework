"""WordSequencsII"""
def word_seq2(word, word2, indexx):
    """print word"""
    while indexx-1 != max(len(word), len(word2)):
        _ = ([print(i, end='') for i in word2[:indexx]], \
            [print(j, end='') for j in word[indexx:]], print())
        indexx += 1
word_seq2([i for i in input()], [j for j in input()], 0)
