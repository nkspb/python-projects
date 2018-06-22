def invest(amount, rate, time):
    """ 
    Track the growing amount of an investment over time
    """
    print("principal amount: ${}".format(amount))
    print("annual rate of return: {}".format(rate))
    for i in range(1, time + 1):
        res = amount + (amount * rate)
        amount = res
        print("year {}: ${}".format(i, res))

while True:
    user_amount = float(input("Enter an amount: "))
    user_rate = float(input("Enter rate: "))
    user_time = int(input("Enter time period: "))

    invest(user_amount, user_rate, user_time)
