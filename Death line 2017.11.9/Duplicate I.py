"""duplicate I"""
def duplicate(first_group, secound_group, duplicated):
    """check duplicated student"""
    first_group = [input() for _ in range(first_group)]
    secound_group = [input() for _ in range(secound_group)]
    for i in first_group:
        if i in secound_group:
            duplicated.append(int(i))
    if len(duplicated) == 0:
        print('Nope')
    else:
        print(*sorted(duplicated, reverse=True), sep='\n')
duplicate(int(input()), int(input()), list())
