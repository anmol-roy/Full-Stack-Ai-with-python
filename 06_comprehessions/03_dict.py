tea_prices_inr = {
    'Green Tea': 150,
    'Black Tea': 120,
    'Oolong Tea': 200,
    'White Tea': 250,
}
tea_prices_usd = {tea: price / 85 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd.float_items(3))  # Output: {'Green Tea': 1.76, 'Black Tea': 1.41, 'Oolong Tea': 2.35, 'White Tea': 2.94}
