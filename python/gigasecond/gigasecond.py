# function to add one giga-second to a give date (1 giga-second is 10**9)

from datetime import timedelta

def add_gigasecond(date):
    return date + timedelta(seconds = 10**9)
