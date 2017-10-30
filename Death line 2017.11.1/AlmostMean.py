"""almost mean"""
def almost(dict_data, mean, amount, ref):
    """find student that score almost mean"""
 
    for i in range(amount):
        data = input().split('\t')
        dict_data[data[0]] = data[1]
 
    for i in dict_data:
        mean += float(dict_data[i])
    mean /= amount
 
    for i in dict_data:
        if float(dict_data[i]) <= mean and float(dict_data[i]) > float(ref):
            ref = dict_data[i]
            student_id = i
    print("%s\t%s" %(student_id, ref))
almost(dict(), 0, int(input()), 0)
