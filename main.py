stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

stock_name = input("Enter Stock Name: ").upper()

print("You selected:", stock_name)

price = stock_prices[stock_name]

print("Stock Price:", price)
quantity = int(input("Enter Quantity: "))

total = price * quantity

print("\n------ Portfolio Summary ------")
print("Stock Name :", stock_name)
print("Price      :", price)
print("Quantity   :", quantity)
print("Total Value:", total)

with open("portfolio.txt", "w") as file:
    file.write("------ Portfolio Summary ------\n")
    file.write(f"Stock Name : {stock_name}\n")
    file.write(f"Price      : {price}\n")
    file.write(f"Quantity   : {quantity}\n")
    file.write(f"Total Value: {total}\n")

print("\nPortfolio saved successfully in portfolio.txt")