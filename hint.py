def hint(range, diff):

    interval = range / 5

    if diff <= (5 * interval) and diff > (4 * interval):
        return("Ice Cold")
    elif diff <= (4 * interval) and diff > (3 * interval):
        return("Cold") 
    elif diff <= (3 * interval) and (diff > 2 * interval):
        return("Neutral")
    elif diff <= (2 * interval) and diff > (1 * interval):
        return("Warm")
    else:
        return("Hot")