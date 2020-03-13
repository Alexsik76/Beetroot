# Create a function which takes as input two dicts with structure mentioned
# above, then computes and returns the total price of stock.
stock1 = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices1 = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def calkulate_total_price(stock=stock1, prices=prices1):
    res = (set(stock.keys()) & set(prices.keys()))
    print(res)
    total_price = 0
    for item in res:
        total_price += (stock[item] * prices[item])
    return total_price


print(f'Total price = {calkulate_total_price()}.')
