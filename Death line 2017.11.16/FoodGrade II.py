"""Food Grade"""
def food(weight, chickens, count, total_weight):
    """food grade"""
    while int(chickens[0]) <= weight and len(chickens) != 1:
        weight -= int(chickens[0])
        count += 1
        total_weight += int(chickens[0])
        del chickens[0]
    if total_weight+int(chickens[0]) <= weight:
        count += 1
        total_weight += int(chickens[0])
    return count
print(food(int(input()), sorted(map(int, input().split())), 0, 0))
