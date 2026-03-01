# practical 4
# Taking input from user
n = int(input("Enter number of items sold: "))
prices = []

for i in range(n):
    price = float(input("Enter price of item: "))
    prices.append(price)

t = tuple(prices)

# a) Total number of items sold
print("Total items sold:", len(t))

# b) Cheapest item price
if len(t) > 0:
    print("Cheapest item price:", min(t))

# c) Costliest item price
    print("Costliest item price:", max(t))

# d) Price list in ascending order
    print("Prices in ascending order:", tuple(sorted(t)))

# e) Number of costliest items sold
    costliest = max(t)
    print("Number of costliest items sold:", t.count(costliest))
else:
    print("No items sold")