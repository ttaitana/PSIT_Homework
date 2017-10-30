"""GCD_n"""
def find_gcd(amount, numbers):
    """find GCD of all number"""
    numbers = [int(input()) for _ in range(amount)]
    for i in range(max(numbers), 0, -1):
        if all([j%i == 0 for j in numbers]):
            print(i)
            break
find_gcd(int(input()), list())
