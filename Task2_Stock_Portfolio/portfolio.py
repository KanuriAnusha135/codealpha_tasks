stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")
print("-----------------------")
print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid number.")

print("\nYour Portfolio")
print("-----------------------")

for stock, quantity in portfolio.items():
    value = stocks[stock] * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${stocks[stock]} = ${value}")

print("-----------------------")
print(f"Total Investment: ${total_investment}")
print("Thank you for using the Stock Portfolio Tracker!")
