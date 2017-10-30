"""perfect"""
def perfect(number, total, position):
    """find perfect number"""
    p_num = 6
    prime = []
    for i in range(2, 100):
        prime.append(checker(i))
 
    while number > p_num:
        total += p_num
        p_num = (2**(prime[position]-1)) * (2**prime[position] - 1)
        position += 1
    print(int(total))
 
def checker(number):
    """check number is prime number?"""
    for i in range(2, int(number**.5)+1):
        if number%i == 0:
            return 0
    return number
 
perfect(int(input()), 0, 1)
