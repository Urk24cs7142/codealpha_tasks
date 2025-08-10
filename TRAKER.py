# Hardcoded stock prices
prices = {"AAPL": 180, "TSLA": 250, "GOOG": 130}

portfolio = {}
total = 0

print("Enter stock holdings (leave blank stock name to finish):")

while True:
    stock = input("Stock symbol: ").upper()
    if stock == "":
        break
    if stock not in prices:
        print("Unknown stock. Available:", ", ".join(prices.keys()))
        continue
    qty = int(input("Quantity: "))
    portfolio[stock] = qty
    total += prices[stock] * qty

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${prices[stock]} = ${prices[stock]*qty}")

print("\nTotal Investment Value: $", total)