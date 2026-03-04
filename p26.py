# reverse copy of array
arr = []

print("Enter 10 integers:")

for i in range(10):
    num = int(input())
    arr.append(num)

# Reverse copy
reverse_arr = arr[::-1]

print("Original Array:", arr)
print("Reversed Array:", reverse_arr)