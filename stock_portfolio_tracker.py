import csv

# Hardcoded dictionary of stock prices (USD)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOG": 140,   # Google
    "MSFT": 310,   # Microsoft
    "AMZN": 130,   # Amazon
}

# Dictionary to store user's portfolio
portfolio = {}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock details (type 'done' to finish):")

# Take user input for stock name and quantity
while True:
    stock_name = input("Enter stock symbol: ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found! Please choose from the available list.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number for quantity.")

# Calculate total investment
total_value = 0
print("\n=== YOUR PORTFOLIO SUMMARY ===")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock} - Quantity: {qty}, Price: ${stock_prices[stock]}, Value: ${value}")

print(f"\n💰 TOTAL INVESTMENT VALUE: ${total_value}")

# Ask user to save results
save_choice = input("\nDo you want to save this report? (y/n): ").lower()

if save_choice == "y":
    print("1. Save as Text (.txt)")
    print("2. Save as CSV (.csv)")
    file_choice = input("Choose file format (1 or 2): ")

    if file_choice == "1":
        with open("portfolio_report.txt", "w") as file:
            file.write("=== STOCK PORTFOLIO REPORT ===\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: Qty={qty}, Price=${stock_prices[stock]}, Value=${value}\n")
            file.write(f"\nTOTAL INVESTMENT VALUE: ${total_value}\n")
        print("✅ Report saved as 'portfolio_report.txt'")

    elif file_choice == "2":
        with open("portfolio_report.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow(["TOTAL", "", "", total_value])
        print("✅ Report saved as 'portfolio_report.csv'")
    else:
        print("❌ Invalid choice. Report not saved.")

print("\nThank you for using the Stock Portfolio Tracker!")
