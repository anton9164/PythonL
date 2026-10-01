def is_pair_supported(pair):
    supported_pairs = ["BTC/USDT", "ETH/USDT", "btc/usdt"]

    if pair in supported_pairs:
        return True
    return False


while True:
    checkinputpair = input("Enter a trading pair (e.g., BTC/USDT): ")
    if is_pair_supported(checkinputpair):
        print(f"The trading pair {checkinputpair} is supported.")
        antpa = input("Would you like to check another pair? (y/n)")
        if antpa.lower() == "y":
            continue
        else:
            print("This is end of the line.")
            break
    else:
        print(f"Trading pair {checkinputpair} is not supported. Please check the pair and try again.")
        checkinputpair = input("Enter a trading pair (e.g., BTC/USDT) or press Enter to exit:")
        if checkinputpair == "":
            print("Exiting the program.")
            break