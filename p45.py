import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("sales_data.csv")

# a) Line Plot (Total Profit)
plt.plot(data["Month"], data["TotalProfit"])
plt.title("Total Profit of All Months")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot (All Products)
plt.plot(data["Month"], data["Facecream"], label="Facecream")
plt.plot(data["Month"], data["Facewash"], label="Facewash")
plt.plot(data["Month"], data["Toothpaste"], label="Toothpaste")
plt.plot(data["Month"], data["Bathingsoap"], label="Bathingsoap")
plt.plot(data["Month"], data["Shampoo"], label="Shampoo")
plt.plot(data["Month"], data["Moisturizer"], label="Moisturizer")

plt.title("Sales Data of Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# c) Bar Chart (Facecream & Facewash)
x = data["Month"]

plt.bar(x, data["Facecream"])
plt.bar(x, data["Facewash"])

plt.title("Facecream & Facewash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# d) Pie Chart (Total yearly sales of each product)
total_sales = [
    data["Facecream"].sum(),
    data["Facewash"].sum(),
    data["Toothpaste"].sum(),
    data["Bathingsoap"].sum(),
    data["Shampoo"].sum(),
    data["Moisturizer"].sum()
]

labels = ["Facecream", "Facewash", "Toothpaste", "Bathingsoap", "Shampoo", "Moisturizer"]

plt.pie(total_sales, labels=labels, autopct="%1.1f%%")
plt.title("Yearly Sales Distribution")
plt.show()