"""Flatten"""
import json as js
def main(list_of_number, answer):
    """main function"""
    for i in list_of_number:
        target = flatten(i, list())
        if isinstance(target, int):
            answer.append(target)
        else:
            for j in target:
                answer.append(j)
    print(sorted(answer, reverse=True))


def flatten(target_var, ans):
    """check and flatten list"""
    if isinstance(target_var, int):
        return target_var
    else:
        for i in target_var:
            checker = flatten(i, ans)
            if isinstance(checker, int):
                ans.append(checker)
        return ans
main(js.loads(input()), list())
