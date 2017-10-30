"""Fibo recursion"""
def fibo(time):
    """find fibo number"""
    if time == 0:
        return 0
    elif time > 1:
        return fibo(time-1) + fibo(time-2)
    else:
        return 1
print(fibo(int(input())))
