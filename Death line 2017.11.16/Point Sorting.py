"""
lelelelelelelelelellelelelellelelelel
lelel       Point Sorting       lelel
lelelelelelelelelelelelelelelelelelel
"""
def controller(answer):
    """caller function"""
    for _ in range(int(input())):
        point_sorter(int(input()), answer)
    _ = [print(*i) for i in answer]

def point_sorter(times, answer):
    """sort sumof equation"""
    sum_equation = list()
    equation = [list(map(int, input().split())) for i in range(times)]

    for i in equation:
        sum_equation.append(sum(i))

    for _ in range(times):
        for i in range(times-1):

            if sum_equation[i] > sum_equation[i+1]:
                equation[i], equation[i+1] = equation[i+1], equation[i]
                sum_equation[i], sum_equation[i+1] = sum_equation[i+1], sum_equation[i]

            elif sum_equation[i] == sum_equation[i+1]:
                if equation[i][1] < equation[i+1][1]:
                    equation[i], equation[i+1] = equation[i+1], equation[i]
                    sum_equation[i], sum_equation[i+1] = sum_equation[i+1], sum_equation[i]

    _ = [answer.append(i) for i in equation]

controller(list())
