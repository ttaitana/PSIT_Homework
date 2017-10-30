"""day2011"""
def day2011(day, month, counting):
    """find day in that tear"""
    day_in_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    amount_of_day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
    for i in range(month-1):
        counting += amount_of_day_in_month[i]
    print(day_in_week[(counting + day)%7 - 1])
day2011(int(input()), int(input()), 0)
