"""Line sorting"""
def line_sort(list_word):
    """return word which sorted by len of word"""
    return sorted(list_word, key=len)
print(*line_sort([input() for i in range(int(input()))]), sep='\n')
