"""CoinChangev1"""
def coin_chenger(money, coin_type, coin):
    """making coin changer"""
    for i in range(4):
        got_coin = money//(coin_type[i])
        money -= got_coin*(coin_type[i])
        coin += got_coin
    return int(coin)
print(coin_chenger(int(input()), [25, 10, 5, 1], 0))
