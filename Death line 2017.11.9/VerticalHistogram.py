"""VerticalHistogram"""
def filter(word, counter):
    final_line = ('   ', *word)
    list_for_print = {}
    for i in word:
        if i in list_for_print:
            list_for_print[i] += 1
        else:
            list_for_print[i] = 1
    print(list_for_print)
filter([i if i.isalpha() else 0 for i in input()], 1)
