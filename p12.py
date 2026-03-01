# Electricity Bill Calculation

cust_no = input("Enter Customer Number: ")
units = int(input("Enter Units Consumed: "))

if units <= 100:
    amount = units * 1
elif units <= 300:
    amount = 100 + (units - 100) * 1.25
elif units <= 500:
    amount = 350 + (units - 300) * 1.50
else:
    amount = 650 + (units - 500) * 1.75

print("\n----- Electricity Bill -----")
print("Customer Number :", cust_no)
print("Units Consumed  :", units)
print("Total Amount to Pay : Rs.", amount)