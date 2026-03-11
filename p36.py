# sum of numbers in numbers.txt
f = open("numbers.txt", "r")

total = 0

for line in f:
    total += int(line.strip())

print("Sum of numbers:", total)

f.close()