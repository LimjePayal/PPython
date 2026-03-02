# maximum and minimum difference pair
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Initialize
max_diff = 0
min_diff = abs(arr[1] - arr[0])
max_pair = ()
min_pair = ()

# Find differences
for i in range(n):
    for j in range(i + 1, n):
        diff = abs(arr[i] - arr[j])

        if diff > max_diff:
            max_diff = diff
            max_pair = (arr[i], arr[j])

        if diff < min_diff:
            min_diff = diff
            min_pair = (arr[i], arr[j])

print("Maximum difference pair:", max_pair)
print("Minimum difference pair:", min_pair)