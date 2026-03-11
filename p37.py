# count how many times the appears in words.txt
f = open("words.txt", "r")

text = f.read().lower()

count = text.count("the")

print("Occurrences of 'the':", count)

f.close()