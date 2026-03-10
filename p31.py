# create name.txt and write name
f = open("names.txt", "w")

f.write("Alice\n")
f.write("Bob\n")
f.write("Charlie\n")

f.close()
print("Names written to file")