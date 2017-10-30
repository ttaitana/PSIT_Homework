"""missing number"""
def missing(number, list_of_number):
    """make list of number"""
    for num in range(1, number+1):
        list_of_number.append(num)
    print(*checker(list_of_number), sep='\n')
 
 
def checker(list_of_number):
    """check number in list if list has that number, remove it"""
    while True:
        pass_out = int(input())
        if pass_out == 0:
            break
        else:
            list_of_number.remove(pass_out)
    return list_of_number
missing(int(input()), list())
