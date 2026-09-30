def is_pair_supported(pair):
    supported_pairs = ["BTC/USDT", "ETH/USDT", "btc/usdt"]

    if pair in supported_pairs:
        return True
    return False

print(is_pair_supported("BTC/USDT"))
print(is_pair_supported("SOL/USDT"))