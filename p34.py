# copy content of source.txt to destination.txt
source = open("source.txt", "r")
dest = open("destination.txt", "w")

data = source.read()
dest.write(data)

source.close()
dest.close()

print("File copied successfully")