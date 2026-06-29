prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 160
}

total = 0

print("=== STOCK TRACKER ===")

while True:
    stock = input("Stock name (or exit): ").upper()

    if stock == "EXIT":
        break

    if stock not in prices:
        print("Not available")
        continue

    qty = int(input("Quantity: "))

    value = prices[stock] * qty
    total += value

print("Total Investment =", total)

with open("portfolio.txt", "w") as f:
    f.write("Total Investment = " + str(total))

print("Saved in portfolio.txt")
