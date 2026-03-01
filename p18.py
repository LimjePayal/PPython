# practical 4
# Taking input from user
n = int(input("Enter number of elements: "))
elements = []

for i in range(n):
    num = int(input("Enter element: "))
    elements.append(num)

t = tuple(elements)

# a) Print total number of items
print("Total number of items:", len(t))

# b) Print last item
if len(t) > 0:
    print("Last item:", t[-1])
else:
    print("Tuple is empty")

# c) Print tuple in reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if 5 is present
if 5 in t:
    print("Yes, 5 is present")
else:
    print("No, 5 is not present")

# e) Remove first and last item and sort remaining
if len(t) > 2:
    new_tuple = tuple(sorted(t[1:-1]))
    print("After removing first and last, sorted tuple:", new_tuple)
else:
    print("Not enough elements to remove first and last")