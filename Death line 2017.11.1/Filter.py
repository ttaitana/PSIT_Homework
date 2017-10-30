"""Filter"""
import json as js
def printer(score, filter_score, score_list):
    """grade filter"""
    score = js.loads(score)
    _ = [score_list.append(i) for i in score]
    score_list.sort()
    count = 0
    for i in score_list:
        if score[i] >= filter_score:
            count += 1
            print("%s\t%.2f" %(i, score[i]))
    if count == 0:
        print('Nope')
printer(input(), float(input()), list())
