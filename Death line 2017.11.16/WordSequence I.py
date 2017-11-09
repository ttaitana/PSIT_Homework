"""WordSequence I"""
def word_seq1(word):
    """print word"""
    _ = [print(word[:i]) for i in range(1, len(word)+1)]
word_seq1(input())
