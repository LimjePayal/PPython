# Program to copy text from one file to another in uppercase

source_file = input("Enter source file name: ")
dest_file = input("Enter destination file name: ")

# Open source file
with open(source_file, "r") as f1:
    data = f1.read()

# Convert to uppercase
data_upper = data.upper()

# Write to new file
with open(dest_file, "w") as f2:
    f2.write(data_upper)

print("Content copied in uppercase successfully.")

# Display new file content
with open(dest_file, "r") as f2:
    print("\nContent of destination file:")
    print(f2.read())