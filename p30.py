# Program to copy python file without comments

source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as f1, open(destination, "w") as f2:
    for line in f1:
        # Skip comment lines
        if not line.strip().startswith("#"):
            f2.write(line)

print("File copied without comments.")

# Print source file content
print("\nSource File Content:")
with open(source, "r") as f:
    print(f.read())

# Print destination file content
print("\nDestination File Content (without comments):")
with open(destination, "r") as f:
    print(f.read())