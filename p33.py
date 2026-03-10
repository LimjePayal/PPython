# count number of characters in data.txt
f = open("data.txt", "r")

data = f.read()
count = len(data)

print("Total characters:", count)

f.close()