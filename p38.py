# Create passed.txt for students with grade A or B
f = open("grades.txt", "r")
p = open("passed.txt", "w")

for line in f:
    parts = line.split()
    name = parts[0]
    grade = parts[1]

    if grade == "A" or grade == "B":
        p.write(name + "\n")

f.close()
p.close()

print("Passed students saved in passed.txt")