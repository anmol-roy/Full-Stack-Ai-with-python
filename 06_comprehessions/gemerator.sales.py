daily_sales = [1500, 2300, 1800, 2200, 2000]
total_sales = sum(sale for sale in daily_sales if sale > 2000)
print(total_sales)  