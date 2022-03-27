def GetMaxMin():
    min = -1
    max = -1
    attempt = 1
    # while loop getting min and max value that is positive

    while min < 0:
        try:
            min = int(input("Min Value: "))
        except ValueError:
            print("Please input a minimum integer that is 0 or greater.")
    while max < min:
        try:
            if attempt == 1:
                max = int(input("Max Value: "))
                attempt = 2
            else:
                max = int(input("Max value must be greater than min value. Max Value: "))
        except ValueError:
            print("Please input an maximum integer greater than the minimum value provided.")

    return (min, max)