"""GCD_v2"""
def gcd_2(num1, num2):
    """find gdc"""
    while num2 != 0:
        num1, num2 = num2, num1%num2
    print(num1)
gcd_2(int(input()), int(input()))
