# Initialize vote count for 5 candidates
# election voting system
count = [0, 0, 0, 0, 0]
spoilt = 0

n = int(input("Enter number of voters: "))

for i in range(n):
    vote = int(input("Enter candidate number (1-5): "))

    if 1 <= vote <= 5:
        count[vote - 1] += 1
    else:
        spoilt += 1

# Display results
for i in range(5):
    print("Votes for Candidate", i + 1, ":", count[i])

print("Number of Spoilt Ballots:", spoilt)