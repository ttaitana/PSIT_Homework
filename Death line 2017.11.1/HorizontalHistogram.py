"""HorizontalHistogram"""
def hirozon(word, alpha_lower, alpah_upper):
    """main founction"""
    for i in word:
        if i.islower():
            if i not in alpha_lower:
                alpha_lower[i] = '-'
            else:
                alpha_lower[i] += '-'
        elif i.upper():
            if i not in alpah_upper:
                alpah_upper[i] = '-'
            else:
                alpah_upper[i] += '-'
    printer(alpha_lower)
    printer(alpah_upper)
 
 
def printer(alpha):
    """print out and sort alphabet"""
    list_of_alpha = list()
    _ = [list_of_alpha.append(i) for i in alpha]
    list_of_alpha.sort()
    for j in list_of_alpha:
        print("%s :" %j, end=' ')
        count = 0
        for i in alpha[j]:
            print(i, end='')
            count += 1
            if count%5 == 0 and count != 0 and count-len(alpha[j]) != 0:
                print('|', end='')
        print()
hirozon(input(), dict(), dict())
