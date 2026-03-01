# sum of all number from 1 to given number
num = int(input("Enter a number: "))
total = 0
i = 1

while i <= num:
    total += i
    i += 1

print("Sum is:", total)