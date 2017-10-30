"""isPrime_large"""
def prime(number):
    """print prime number"""
    if number > 2:
        print(checker(number))
    elif number == 2:
        print("YES")
    else:
        print("NO")
 
 
def checker(number):
    """check number is prime number?"""
    for i in range(2, int(number**.5)+1):
        if number%i == 0:
            return 'NO'
    return "YES"
 
prime(int(input()))
