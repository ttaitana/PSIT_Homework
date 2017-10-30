"""sqFree"""
def sqfree(number, counter):
    """find square free"""
    for i in range(1, number+1):
        counter += sqfree_checker(i)
    print(counter)
 
 
def sqfree_checker(number):
    """check number is prime number?"""
    if number < 4:
        return 1
 
    for i in range(2, int(number**.5)+1):
        if number%(i**2) == 0:
            return 0
    return 1
sqfree(int(input()), 0)
