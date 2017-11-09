"""Diamond"""
def diamond(level, row, mine_data):
    """find max value"""
    compair = [0]*row
    for i in range(level):
        mine_data[i] = list(map(int, input().split()))
    for i in range(level):
        for j in range(row):
            compair[j] += mine_data[i][j]
    print(max(compair))
diamond(int(input()), int(input()), dict())
