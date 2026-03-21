import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("Complete Book Report:")
print(df)

# b) Books by given author
author_name = input("Enter author name: ")
print("\nBooks by Author:")
print(df[df['Author'] == author_name])

# c) Books by given publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by Publisher:")
print(df[df['Publisher'] == publisher_name])

# d) Cheapest and costliest book
cheapest = df.loc[df['Price'].idxmin()]
costliest = df.loc[df['Price'].idxmax()]

print("\nCheapest Book:")
print(cheapest['Title'])

print("\nCostliest Book:")
print(costliest['Title'])

# e) Sort by year
print("\nBooks sorted by Year:")
print(df.sort_values(by='Year'))