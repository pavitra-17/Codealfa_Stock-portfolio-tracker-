stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 130
}

total_investment = 0

print("📈 Stock Portfolio Tracker")

while True:

    stock_name = input("\nEnter stock name (or type 'done'): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print("Investment added:", investment)

print("\nTotal Investment Value =", total_investment)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Data saved to portfolio.txt")
